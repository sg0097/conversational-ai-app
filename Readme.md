# Conversational AI App

This is a conversational AI application that integrates multiple language models (Gemini and Groq) to generate intelligent responses. The app provides a chat interface where users can communicate with AI, switch between models, and receive relevant answers to their queries.

## Features

- **Model Switching**: Users can choose between different AI models (Gemini, Groq) for the conversation.
- **Multiple Conversations**: Each user interaction is treated as a separate conversation, maintaining context.
- **Real-time Chat**: Users can chat with the AI in real-time, and responses are generated dynamically.
- **User-friendly Interface**: Built with Gradio, providing an interactive chat experience.
- **API Integration**: The app communicates with the backend API to switch models and handle chat interactions.

## Prerequisites

- Python 3.8+
- FastAPI
- Gradio
- Requests
- dotenv
- Any AI models (Gemini and Groq)

## Setup

1. Clone the repository
Clone this repository to your local machine.

```bash
git clone https://github.com/sg0097/conversational-ai-app.git
cd conversational-ai-app
python -m venv venv
venv/Scripts/activate

2. pip install -r requirements.txt


3. Set up environment variables
   Create a .env file in the project root and add your API keys for Gemini and Groq:
      GEMINI_API_KEY=your_gemini_api_key
      GROQ_API_KEY=your_groq_api_key


4. Run the Backend API
   uvicorn main:app --reload (The backend will be running on http://localhost:5000)

   for testing the api calls:
    1. set_model:
    curl -X POST "http://localhost:5000/set_model" -H "Content-Type: application/json" -d "{\"model_name\": \"groq\"}"
     OUTPUT =>{"message":"Model switched to groq"}

    2. chat:
    curl -X POST "http://localhost:5000/chat" -H "Content-Type: application/json" -d "{\"prompt\": \"Prime Minister of india?\"}"
     OUTPUT => {"response":"The current Prime Minister of India is Narendra Modi.\n"}

5.Run the Gradio Frontend
  python app.py (The Gradio app will be accessible at http://localhost:7860)


