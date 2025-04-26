import httpx
from app.config import GROQ_API_KEY

class GroqClient:
    async def chat(self, prompt: str) -> str:
        # Simulated response (replace with real API call if needed)
        return f"[Groq AI]: {prompt.upper()}"  # Uppercase prompt for demo
