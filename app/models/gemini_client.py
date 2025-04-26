import httpx
from app.config import GEMINI_API_KEY

class GeminiClient:
    async def chat(self, prompt: str) -> str:
        url = "https://gemini.api.endpoint"  # Replace with actual Gemini API endpoint
        headers = {
            "Authorization": f"Bearer {GEMINI_API_KEY}",
            "Content-Type": "application/json",
        }
        payload = {
            "prompt": prompt,
            "max_tokens": 150,  # Adjust as needed
            "temperature": 0.7,  # Adjust as needed
        }
        
        async with httpx.AsyncClient() as client:
            response = await client.post(url, json=payload, headers=headers)
        
        # Check if the response is valid
        if response.status_code == 200:
            result = response.json()  # Assuming the response is in JSON format
            return result.get("response", "No response field found.")
        else:
            return f"Error: {response.status_code} - {response.text}"
