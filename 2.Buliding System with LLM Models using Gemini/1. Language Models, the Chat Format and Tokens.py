import os
from pathlib import Path
from google import genai
from dotenv import load_dotenv

load_dotenv(Path(__file__).with_name(".env"))

api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GOOGLE_API_KEY is not set. Add it to your .env file.")

client = genai.Client(api_key="AIzaSyBb1BdJ9pPbjeHT9LXvKyOpvcVnOzG3-ys")

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Explain AI in simple words"
)

print(response.text)
