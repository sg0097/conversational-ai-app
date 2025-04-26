# test_groq.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()

GROQ_API_KEY = os.getenv("GROQ_API_KEY")
print("Groq Key:", GROQ_API_KEY)

def call_groq(prompt: str, model="llama3-70b-8192"):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json",
    }
    data = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": prompt}
        ]
    }

    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        output = response.json()
        reply = output["choices"][0]["message"]["content"]
        return reply
    else:
        print(response.text)
        raise Exception(f"Groq API Error: {response.status_code}")

if __name__ == "__main__":
    prompt = "current Prime minister of india" 
    reply = call_groq(prompt)
    print("Groq says:", reply)
