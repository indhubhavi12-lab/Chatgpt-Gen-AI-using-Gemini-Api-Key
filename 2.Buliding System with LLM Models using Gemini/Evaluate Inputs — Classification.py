import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("Enter your API Key"))

model = genai.GenerativeModel("gemini-2.5-flash")

text = """
I love this product. It works perfectly and delivery was fast.
"""

prompt = f"""
Classify the sentiment of the following text as:
Positive, Negative, or Neutral.

Text:
{text}
"""

response = model.generate_content(prompt)

print("Classification Result:")
print(response.text)
