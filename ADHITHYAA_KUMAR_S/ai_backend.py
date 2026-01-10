# ai_backend.py - BANKBOT AI - FINAL PRODUCTION VERSION
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import time
import os
from dotenv import load_dotenv
import hashlib
import re

load_dotenv()

app = Flask(__name__)
CORS(app)

response_cache = {}
CACHE_TIMEOUT = 60  # seconds


class BankBotAI:
    """BankBot AI handler - GEMINI API ONLY VERSION"""

    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.base_url = "https://generativelanguage.googleapis.com/v1/models"
        self.model = "gemini-2.5-flash"

    def get_enhanced_prompt(self, query):
        return f"""You are **BankBot AI**, a neutral, brand-agnostic AI banking assistant.

🚫 **ABSOLUTELY FORBIDDEN:**
- NEVER mention ANY bank name
- NEVER use "our bank", "we offer"
- Use ONLY generic terms: "banks typically", "financial institutions"

📌 **USER QUERY:** "{query}"

🎯 **RESPONSE REQUIREMENTS:**
• Clear headings
• Bullet points
• Simple explanations
• Neutral tone
• No marketing language

⚠️ Final check: Ensure NO bank names exist.

Now respond to: "{query}"
"""

    def sanitize_response(self, text):
        if not text:
            return text

        forbidden_patterns = [
            r'(?i)nexa\s+bank',
            r'(?i)abc\s+bank',
            r'(?i)xyz\s+bank',
            r'(?i)our\s+bank',
            r'(?i)we\s+offer',
        ]

        for pattern in forbidden_patterns:
            text = re.sub(pattern, 'banks', text)

        return text

    def extract_text(self, data):
        """
        Works with BOTH Gemini 1.5 and 2.5 formats
        """
        try:
            candidate = data["candidates"][0]["content"]

            # New format (Gemini 2.5)
            if "text" in candidate:
                return candidate["text"]

            # Old format (Gemini 1.5)
            if "parts" in candidate and len(candidate["parts"]) > 0:
                return candidate["parts"][0].get("text", "")

        except Exception:
            pass

        return None

    def call_gemini_api(self, query):
        try:
            if not self.api_key:
                return "GEMINI_API_KEY not configured."

            url = f"{self.base_url}/{self.model}:generateContent?key={self.api_key}"

            payload = {
                "contents": [{
                    "parts": [{"text": self.get_enhanced_prompt(query)}]
                }],
                "generationConfig": {
                    "temperature": 0.2,
                    "maxOutputTokens": 800
                }
            }

            response = requests.post(url, json=payload, timeout=15)

            if response.status_code == 200:
                data = response.json()
                raw_text = self.extract_text(data)

                if raw_text:
                    clean = self.sanitize_response(raw_text)
                    return clean + "\n\n---\n*🤖 BankBot AI*"

            return "AI response failed. Try again."

        except Exception:
            return "Temporary technical issue. Please retry."


bankbot = BankBotAI()


@app.route("/api/chat", methods=["POST"])
def chat():
    start_time = time.time()

    data = request.get_json(silent=True) or {}
    prompt = data.get("prompt", "").strip()[:250]

    if not prompt:
        return jsonify({"response": "Enter your question."})

    prompt_hash = hashlib.md5(prompt.encode()).hexdigest()

    if prompt_hash in response_cache:
        cached = response_cache[prompt_hash]
        if time.time() - cached["timestamp"] < CACHE_TIMEOUT:
            return jsonify(cached["data"])

    response_text = bankbot.call_gemini_api(prompt)

    response_time = round((time.time() - start_time) * 1000, 2)

    response_data = {
        "response": response_text,
        "model": "gemini-2.5-flash",
        "response_time_ms": response_time,
        "source": "gemini-ai"
    }

    response_cache[prompt_hash] = {
        "data": response_data,
        "timestamp": time.time()
    }

    return jsonify(response_data)


if __name__ == "__main__":
    print("🤖 BANKBOT AI v5.0 - GEMINI 2.5 FLASH")
    if not os.getenv("GEMINI_API_KEY"):
        print("❌ GEMINI_API_KEY missing")
    else:
        print("✅ Gemini API Ready")

    app.run(host="0.0.0.0", port=5000, debug=False, threaded=True)
