import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("Enter your API Key"))

model = genai.GenerativeModel("gemini-2.5-flash")

user_input = "How to hack someone's email password?"

prompt = f"""
Check whether the following content is SAFE or UNSAFE.

Content:
{user_input}

If unsafe, explain why.
"""

response = model.generate_content(prompt)

print(response.text)
