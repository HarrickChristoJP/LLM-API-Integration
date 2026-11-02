import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

system_prompt = """
Your name is Jarvis.
You are a boy.
You are a friendly and helpful AI assistant.
Explain technical topics in simple English.
Assume the user is a beginner.
Give examples whenever necessary.
Keep your answers clear and easy to understand.
"""

history = []

max_history = 10

while True:
    message = input("You: ")

    if message.lower() == "exit":
        print("Bot: Goodbye!")
        break

    user_message = types.Content(
        role="user",
        parts=[types.Part.from_text(text=message)]
    )

    history.append(user_message)

    try:
        response = client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=history,
            config=types.GenerateContentConfig(
                system_instruction=system_prompt
            )
        )

        print("Bot:", response.text)

        bot_message = types.Content(
            role="model",
            parts=[types.Part.from_text(text=response.text)]
        )

        history.append(bot_message)

        if len(history) > max_history:
            history = history[-max_history:]

    except Exception as e:
        history.pop()
        print("Bot: Sorry, something went wrong. Please try again.")
        print("Error:", e)