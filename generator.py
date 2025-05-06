import os
from dotenv import load_dotenv
import google.generativeai as genai

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if api_key is None:
    raise ValueError(
        "❌ GEMINI_API_KEY not found. Please check your `.env` file.")

genai.configure(api_key=api_key)
print("🔑 Loaded Gemini API Key:", api_key[:5], "...")

# Use a known working model ID
model = genai.GenerativeModel(model_name="models/gemini-1.5-pro-latest")


def generate_response(query, tickets):
    context = "\n".join([f"{t['title']} - {t['resolution']}" for t in tickets])

    prompt = f"""You are a helpful support assistant.

Support query: "{query}"
Relevant past tickets:
{context}

Generate a helpful support response based on the above."""

    try:
        response = model.generate_content(prompt)
        return response.text.strip()

    except Exception as e:
        return f"⚠️ An error occurred while generating the response: {str(e)}"
