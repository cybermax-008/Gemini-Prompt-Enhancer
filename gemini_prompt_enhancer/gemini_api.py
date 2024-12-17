import google.generativeai as genai
from dotenv import load_dotenv
import os
load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

def generate_text(prompt):
    """
    Generates text using the Gemini Pro model.

    Args:
        prompt (str): The input prompt.

    Returns:
        str: The generated text.
    """

    model = genai.GenerativeModel('gemini-2.0-flash-exp')
    response = model.generate_content(prompt)
    return response.text