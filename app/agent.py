from app.models.model_manager import ModelManager

class ChatAgent:
    def __init__(self):
        self.model_manager = ModelManager()
        self.history = []

    async def chat(self, prompt: str) -> str:
        self.history.append({"role": "user", "content": prompt})
        full_context = self.get_context()
        response = await self.model_manager.chat(full_context)
        self.history.append({"role": "ai", "content": response})
        return response

    def get_context(self) -> str:
        # Just concatenate last few messages
        return "\n".join([f"{m['role']}: {m['content']}" for m in self.history[-5:]])

    def set_model(self, model_name: str):
        return self.model_manager.set_model(model_name)
