import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(api_key=os.getenv("AIzaSyC-Tg-JSG90eQIPxf34rcIwzklTFYIWLro"))

model = genai.GenerativeModel("gemini-2.5-flash")

# First Prompt
prompt1 = "Explain Machine Learning in one paragraph."

response1 = model.generate_content(prompt1)

summary = response1.text

print("Step 1 Output:\n")
print(summary)

# Second Prompt
prompt2 = f"""
Convert the following explanation into 5 bullet points:

{summary}
"""

response2 = model.generate_content(prompt2)

print("\nStep 2 Output:\n")
print(response2.text)
