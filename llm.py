import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def gemini_chat(prompt):
    model = genai.GenerativeModel('models/gemini-1.5-flash-latest')  # Switch here!
    response = model.generate_content(prompt)
    return response.text
