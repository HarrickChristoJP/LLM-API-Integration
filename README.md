# Jarvis AI Chatbot 

A conversational AI chatbot built using Python, FastAPI, and Google's Gemini API. Jarvis can understand user messages, maintain conversation history, and respond with a friendly personality.

## Features

- **AI-powered responses:** Uses Google's Gemini API to generate responses.
- **Conversation memory:** Remembers previous messages within a conversation.
- **Conversation isolation:** Maintains separate histories using unique conversation IDs.
- **Context management:** Retains the latest 10 messages to manage conversation history.
- **Custom system prompt:** Configured with a friendly assistant personality.
- **Web interface:** Simple chat interface built using HTML, CSS, and JavaScript.
- **Error handling:** Returns readable error messages when the AI service is unavailable.
- **Terminal interface:** Also supports chatting through the Python terminal.

## Technologies Used

- Python
- Google Gemini API
- Google GenAI SDK
- FastAPI
- Uvicorn
- HTML
- CSS
- JavaScript

## Project Structure

```text
ai-chatbot/
│
├── main.py
├── server.py
├── index.html
├── requirements.txt
├── .env
├── .env.example
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd ai-chatbot
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

For Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Configure your API key

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Get your API key from Google AI Studio.

### 6. Run the application

Start the FastAPI server:

```bash
python -m uvicorn server:app --reload
```

Open your browser and visit:

```text
http://127.0.0.1:8000/
```

To access the API documentation:

```text
http://127.0.0.1:8000/docs
```

## API Endpoint

### POST /chat

Accepts a user message and returns an AI-generated response.

**Request:**

```json
{
    "conversation_id": "user123",
    "message": "Hello Jarvis!"
}
```

**Response:**

```json
{
    "conversation_id": "user123",
    "reply": "Hello! How can I help you today?"
}
```

The conversation ID is used to maintain separate conversation histories.

## Context Management

Jarvis stores conversation messages using a Python dictionary.

Each conversation has its own unique ID. The application retains the latest 10 message entries and removes older entries when the limit is exceeded.

Conversation histories are currently stored in memory and reset when the backend server restarts.

## Security

- API keys are stored in environment variables.
- The `.env` file is excluded from Git using `.gitignore`.
- Never upload your actual API key to GitHub.

## Author

Developed as part of an AI and Generative AI internship project.
