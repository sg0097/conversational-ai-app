from app.models.gemini_client import GeminiClient
from app.models.groq_client import GroqClient
from app.config import DEFAULT_MODEL

class ModelManager:
    def __init__(self):
        self.current_model = DEFAULT_MODEL
        self.gemini_client = GeminiClient()
        self.groq_client = GroqClient()

    async def chat(self, prompt: str) -> str:
        if self.current_model == "gemini":
            return await self.gemini_client.chat(prompt)
        elif self.current_model == "groq":
            return await self.groq_client.chat(prompt)
        else:
            return "Unknown model selected."

    def set_model(self, model_name: str):
        if model_name in ["gemini", "groq"]:
            self.current_model = model_name
            return f"Model switched to {model_name}."
        else:
            return "Invalid model name."
