# 🏦 BankBot – Banking AI Assistant

BankBot is a **banking-only AI chatbot** built using **Streamlit** and **Ollama (Local LLM)**.

## 🚀 Features
- Banking-only AI (strict domain control)
- Rule-based + AI hybrid responses
- Persistent chat history (JSON)
- Local LLM (Qwen via Ollama)
- Secure sidebar for balance & account info
- Chat history search
- Offline-capable AI

## 🧠 Tech Stack
- Python
- Streamlit
- Ollama (Qwen model)
- REST API
- JSON-based knowledge library

## 📁 Project Files
- `app.py` – Main application
- `banking_library.json` – Banking rule library
- `requirements.txt` – Dependencies
- `LICENSE` – MIT License

## ▶️ Run Locally
```bash
pip install -r requirements.txt
streamlit run app.py
