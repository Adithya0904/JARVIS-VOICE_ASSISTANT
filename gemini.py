import google.generativeai as genai
import pyttsx3
engine=pyttsx3.init()

def computeMessage(input):
    genai.configure(api_key="AIzaSyBo_c16BFRDJbBIvOYMFSRFYMSSM41kzHM")

    generation_config = {
    "temperature": 0,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
    }

    model = genai.GenerativeModel(
    model_name="gemini-1.5-flash",
    generation_config=generation_config,
    )

    chat_session = model.start_chat(
    history=[
    ]
    )

    response = chat_session.send_message(input)

    return response.text
