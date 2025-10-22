import fitz  # PyMuPDF
import os
import requests
from dotenv import load_dotenv

load_dotenv()

EURI_API_KEY = os.getenv("EURI_API_KEY")
EURI_URL = "https://api.euron.one/api/v1/euri/chat/completions"
MODEL_NAME = "gpt-4.1-nano"  # or any other model available


def extract_text_from_pdf(uploaded_file):
    """Extract text from PDF."""
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text


def ask_euri(prompt, max_tokens=500, temperature=0.5):
    """Send prompt to EURI API and return response."""
    headers = {
        "Authorization": f"Bearer {EURI_API_KEY}",
        "Content-Type": "application/json"
    }

    payload = {
        "messages": [{"role": "user", "content": prompt}],
        "model": MODEL_NAME,
        "max_tokens": max_tokens,
        "temperature": temperature
    }

    response = requests.post(EURI_URL, headers=headers, json=payload)
    response.raise_for_status()
    data = response.json()
    return data["choices"][0]["message"]["content"]
