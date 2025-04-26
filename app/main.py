from fastapi import FastAPI, Request
import os
import requests
from dotenv import load_dotenv
load_dotenv()
app = FastAPI()

model_name = "groq"  # Default model
conversation_history = []

print("Gemini API Key:", os.getenv("GEMINI_API_KEY"))


# Load API Keys from env
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")



def call_gemini(prompt: str, history=[]) -> str:
    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-pro-latest:generateContent?key={GEMINI_API_KEY}"
    
    contents = []
    for item in history:
        contents.append({"parts": [{"text": item["user"]}]})
        contents.append({"parts": [{"text": item["ai"]}]})
    
    # Add new prompt
    contents.append({"parts": [{"text": prompt}]})
    
    payload = {
        "contents": contents
    }
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        candidates = response.json()["candidates"]
        return candidates[0]["content"]["parts"][0]["text"]
    else:
        raise Exception(f"Gemini API Error: {response.status_code}, {response.text}")


def call_groq(prompt: str, history=[], model="llama3-70b-8192") -> str:
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    
    messages = []
    for item in history:
        messages.append({"role": "user", "content": item["user"]})
        messages.append({"role": "assistant", "content": item["ai"]})
    
    # Add new user prompt
    messages.append({"role": "user", "content": prompt})
    
    payload = {
        "model": model,
        "messages": messages
    }
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        return response.json()["choices"][0]["message"]["content"]
    else:
        raise Exception(f"Groq API Error: {response.status_code}, {response.text}")


def generate_response(prompt: str, history=[]) -> str:
    global model_name
    if model_name == "Gemini":
        return call_gemini(prompt, history)
    elif model_name == "groq":
        return call_groq(prompt, history)
    else:
        return "Invalid model selected."

print(model_name)

@app.post("/chat")
async def chat_with_model(request: Request):
    data = await request.json()
    print(f"Received data: {data}")  # Debugging line
    prompt = data.get("prompt")
    history = data.get("history", [])
    
    response = generate_response(prompt, history)
    
    print(f"AI Response: {response}")  # Debugging line
    return {"response": f"[{model_name}] {response}"}



@app.post("/set_model")
async def set_model(request: Request):
    global model_name
    data = await request.json()
    new_model = data.get("model_name")
    
    if new_model in ["Gemini", "groq"]:
        model_name = new_model
        return {"message": f"Model switched to {new_model}"}
    else:
        return {"message": "Invalid model name"}
