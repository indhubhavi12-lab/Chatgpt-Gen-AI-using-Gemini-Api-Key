import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("Enter your API Key"))

model = genai.GenerativeModel("gemini-2.5-flash")

question = """
A train travels 60 km in 1 hour.
How far will it travel in 5 hours?
Explain step by step.
"""

response = model.generate_content(question)

print(response.text)
