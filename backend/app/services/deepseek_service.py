import os
from openai import OpenAI
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Initialize OpenAI Client for DeepSeek
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),  # Your API key from .env
    base_url="https://api.deepseek.com"
)

def summarise_text(text: str) -> str:
    """
    Sends text to DeepSeek API for summarization and returns the summarized version.
    """
    if not text.strip():
        return "Error: Empty text provided for summarization."

    try:
        response = client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {"role": "system", "content": "You are an AI that provides concise summaries."},
                {"role": "user", "content": f"Summarize this: {text}"},
            ],
            stream=False
        )

        return response.choices[0].message.content if response.choices else "Error: No summary generated."
    except Exception as e:
        return f"Error: {str(e)}"