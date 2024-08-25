import speech_recognition as sr
import pyttsx3 
import webbrowser
import musiclibrary
from newsapi import NewsApiClient
import gemini


engine=pyttsx3.init()

api_key="7adc48a8b6614f1290a28b9c2db4e9e6"
newsapi=NewsApiClient(api_key)

def speak(text):
    engine.say(text)
    engine.runAndWait()

def processing(input):
    if(input.lower()=="open youtube"):
        speak("opening youtube")
        webbrowser.open("https://www.youtube.com/")
    elif(input.lower()=="open google"):
        speak("opening google")
        webbrowser.open("https://www.google.co.in/")
    elif(input.lower()=="open stream"):
        speak("opening streamio")
        webbrowser.open("https://web.stremio.com/")
    elif(input.lower()=="open cinema"):
        speak("opening jiocinema")
        webbrowser.open("https://www.jiocinema.com/")

    elif(input.lower().startswith("play")):
        name=input.split("play")[-1]
        print(name)
        speak(f"playing {name}")
        link=musiclibrary.music[name.lower()]
        webbrowser.open(link)

    elif(input.lower()=="get news"):
        top_headlines = newsapi.get_top_headlines(q='cricket',
                                            category='sports',
                                            language='en',
                                            country='in')  # Set country to India

        # Function to print headlines in text format
        
        if top_headlines['status'] == 'ok':
            articles = top_headlines['articles']
            for article in articles:
                speak(article['title'])
        else:
            speak("Failed to fetch headlines")

    else:
        output=gemini.computeMessage(input)
        speak(output)


if __name__=="__main__":
    speak("Initializing Jarvis...")
    while True:
        # Initialize recognizer class (for recognizing speech)
        r=sr.Recognizer()

        with sr.Microphone() as source:
            
            print("Say, Jarvis")
            try:
            #obtain audio from microphone
                audio=r.listen(source,timeout=2,phrase_time_limit=4)
            # recognize speech using google
                sentence=r.recognize_google(audio)
        
                if("jarvis" in sentence.lower()):
                    speak("Yess Master!!")
                    print("Give me a command......")

                    with sr.Microphone() as source:
                        command=r.listen(source,timeout=4,phrase_time_limit=5)
                        processing(r.recognize_google(command))
                
            except Exception as e:
                print(e)

