import gradio as gr
import requests

# Backend server URL
BACKEND_URL = "https://conversational-ai-app.onrender.com/"

# Function to call /set_model API
def set_model(model_name):
    response = requests.post(f"{BACKEND_URL}/set_model", json={"model_name": model_name})
    if response.status_code == 200:
        return f"✅ Model switched to {model_name}"
    else:
        return "❌ Failed to switch model."

# Function to call /chat API
def chat_with_ai(user_message, chat_history, system_prompt):
    # Combine system prompt + user message
    full_prompt = system_prompt + "\n\n" + user_message if system_prompt else user_message
    
    response = requests.post(f"{BACKEND_URL}/chat", json={"prompt": full_prompt})
    if response.status_code == 200:
        ai_message = response.json()["response"]
        chat_history.append((user_message, ai_message))
        return "", chat_history
    else:
        chat_history.append((user_message, "❌ Error from server"))
        return "", chat_history

# Clear chat history
def clear_chat():
    return [], ""

# Gradio UI
with gr.Blocks() as demo:
    gr.Markdown("# 🤖 Conversational AI App")

    model_selector = gr.Dropdown(
        choices=["Gemini", "groq"],
        label="Select Model",
        value="Gemini"
    )

    model_status = gr.Textbox(label="Model Switch Status", interactive=False)

    system_prompt = gr.Textbox(
        label="System Prompt (Optional)",
        placeholder="e.g., 'You are a helpful assistant.'",
        lines=2
    )

    chatbot = gr.Chatbot()

    with gr.Row():
        user_input = gr.Textbox(placeholder="Type your message here...", label="Your Message")
        send_button = gr.Button("Send")
        clear_button = gr.Button("Clear Chat")

    # Model switching
    model_selector.change(set_model, inputs=model_selector, outputs=model_status)

    # Send message
    send_button.click(chat_with_ai, inputs=[user_input, chatbot, system_prompt], outputs=[user_input, chatbot])

    # Clear chat
    clear_button.click(clear_chat, outputs=[chatbot, user_input])

# Run Gradio app
demo.launch(server_name="127.0.0.1", server_port=7860)

