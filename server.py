
import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai
from google.genai import types
from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from pydantic import BaseModel

# Load environment variables
load_dotenv()

# Connect to Gemini
client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# Create FastAPI application
app = FastAPI(title="Jarvis AI Assistant")

# Get project folder location
BASE_DIR = Path(__file__).resolve().parent

# System prompt
system_prompt = """
Your name is Jarvis.
You are a boy.
You are a friendly and helpful AI assistant.
Explain technical topics in simple English.
Assume the user is a beginner.
Give examples whenever necessary.
Keep your answers clear and easy to understand.
"""

# Store conversations separately
conversations = {}

max_history = 10


# Homepage route
@app.get("/")
def home():
    return FileResponse(BASE_DIR / "index.html")


# Request structure
class ChatRequest(BaseModel):
    conversation_id: str
    message: str


# Chat API endpoint
@app.post("/chat")
def chat(request: ChatRequest):

    conversation_id = request.conversation_id
    message = request.message

    # Create a new conversation if needed
    if conversation_id not in conversations:
        conversations[conversation_id] = []

    history = conversations[conversation_id]

    # Add user message
    user_message = types.Content(
        role="user",
        parts=[types.Part.from_text(text=message)]
    )

    history.append(user_message)

    try:
        # Generate response using Gemini
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=history,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt
            )
        )

        reply = response.text or "Sorry, I couldn't generate a response."

        # Add Jarvis response to history
        bot_message = types.Content(
            role="model",
            parts=[types.Part.from_text(text=reply)]
        )

        history.append(bot_message)

        # Keep only the latest 10 messages
        if len(history) > max_history:
            history = history[-max_history:]

        conversations[conversation_id] = history

        return {
            "conversation_id": conversation_id,
            "reply": reply
        }

    except Exception as e:
        # Remove failed user message
        history.pop()

        raise HTTPException(
            status_code=503,
            detail="AI service is temporarily unavailable. Please try again."
        )
