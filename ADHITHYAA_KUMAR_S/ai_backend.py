# ai_backend.py - SIMPLE VERSION
from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import time

app = Flask(__name__)
CORS(app)

@app.route('/api/chat', methods=['POST'])
def chat():
    """Simple direct proxy to Ollama"""
    try:
        data = request.json
        prompt = data.get('prompt', '')
        model = data.get('model', 'llama3')
        
        if not prompt:
            return jsonify({"error": "No query provided"}), 400
        
        # Simple banking system prompt
        banking_prompt = """You are NEXA BANK AI assistant. Answer banking questions briefly (2-3 sentences).
        Focus on: balances, transfers, loans, cards, investments.
        If not banking, say "I specialize in banking only"."""
        
        response = requests.post(
            'http://localhost:11434/api/chat',
            json={
                "model": model,
                "messages": [
                    {"role": "system", "content": banking_prompt},
                    {"role": "user", "content": prompt}
                ],
                "stream": False,
                "options": {
                    "temperature": 0.3,
                    "num_predict": 150  # Very short responses
                }
            },
            timeout=10  # Short timeout
        )
        
        if response.status_code == 200:
            data = response.json()
            return jsonify({
                "response": data["message"]["content"],
                "model": model,
                "timestamp": time.time()
            })
        else:
            return jsonify({"error": "Ollama error"}), 500
            
    except requests.exceptions.Timeout:
        return jsonify({"error": "Ollama timeout - try simpler question"}), 408
    except requests.exceptions.ConnectionError:
        return jsonify({"error": "Ollama not running - start with: ollama run llama3"}), 503
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/health', methods=['GET'])
def health():
    """Simple health check"""
    try:
        response = requests.get('http://localhost:11434/api/tags', timeout=3)
        return jsonify({
            "status": "ok",
            "ollama": "connected",
            "message": "Ready for banking queries"
        })
    except:
        return jsonify({
            "status": "error",
            "ollama": "not_connected",
            "message": "Start Ollama: ollama run llama3"
        }), 503

if __name__ == '__main__':
    print("Simple Banking AI Backend")
    print("Port: 5000")
    print("Make sure Ollama is running: ollama run llama3")
    app.run(host='0.0.0.0', port=5000, debug=False, threaded=True)  