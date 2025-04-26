# test_gemini.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def call_gemini(prompt: str):
    url = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro-latest:generateContent"
    headers = {"Content-Type": "application/json"}
    params = {"key": GEMINI_API_KEY}
    data = {
        "contents": [
            {
                "parts": [{"text": prompt}]
            }
        ]
    }

    response = requests.post(url, headers=headers, params=params, json=data)
    if response.status_code == 200:
        output = response.json()
        reply = output["candidates"][0]["content"]["parts"][0]["text"]
        return reply
    else:
        print(response.text)
        raise Exception(f"Gemini API Error: {response.status_code}")

if __name__ == "__main__":
    prompt = "Prime minister of INdia"
    reply = call_gemini(prompt)
    print("Gemini says:", reply)
