# BANKBOT - FINAL MILESTONE (BANKING ONLY)
# New Chat = clears screen only
# Clear Chat = deletes stored history
# RULE + AI HYBRID (STRICT DOMAIN)

import streamlit as st
import requests
import json
import os
import pyttsx3
from datetime import datetime

# -----------------------------
# CONFIG
# -----------------------------
MODEL_NAME = "qwen2.5:0.5b"
SYSTEM_PROMPT = (
    "You are a banking assistant. "
    "Answer ONLY banking-related questions clearly and professionally."
)

CHAT_FILE = "chat_history.json"
BANK_LIB_FILE = "banking_library.json"

# -----------------------------
# LOAD BANK LIBRARY
# -----------------------------
with open(BANK_LIB_FILE, "r", encoding="utf-8") as f:
    BANK_LIBRARY = json.load(f)

# -----------------------------
# BANKING KEYWORDS (FINAL GATE)
# -----------------------------
BANKING_KEYWORDS = {
    "bank", "account", "balance", "loan", "emi", "interest",
    "deposit", "withdraw", "atm", "card", "debit", "credit",
    "ifsc", "branch", "cheque", "fd", "rd",
    "fixed deposit", "recurring deposit",
    "kyc", "passbook", "statement", "transaction",
    "savings", "current"
}

def is_banking_question(text: str) -> bool:
    text = text.lower()
    return any(k in text for k in BANKING_KEYWORDS)

# -----------------------------
# CHAT STORAGE
# -----------------------------
def load_all_sessions():
    if not os.path.exists(CHAT_FILE):
        return {"sessions": []}
    with open(CHAT_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_all_sessions(data):
    with open(CHAT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

def save_current_chat():
    if st.session_state.current_chat:
        data = load_all_sessions()
        data["sessions"].append({
            "time": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "messages": st.session_state.current_chat
        })
        save_all_sessions(data)
        
        


# -----------------------------
# BANK DATA
# -----------------------------
ACCOUNTS = [
    {"account_number": "1001", "name": "Surya Jai", "pin": "1234", "balance": 50234.75},
    {"account_number": "1002", "name": "Ravi Kumar", "pin": "5678", "balance": 28900.00},
    {"account_number": "1003", "name": "Anitha Devi", "pin": "4321", "balance": 74000.50},
]

def find_account(acc_no):
    return next((a for a in ACCOUNTS if a["account_number"] == acc_no), None)

# -----------------------------
# RULE-BASED BANK LIBRARY
# -----------------------------
def check_bank_library(text):
    t = text.lower()

    # 1️⃣ First: try STRONG (exact / long keyword) matches
    for item in BANK_LIBRARY.values():
        for kw in item["keywords"]:
            if kw in t and len(kw.split()) > 1:
                return item["answer"]

    # 2️⃣ Then: allow generic match ONLY if question is short
    if len(t.split()) <= 3:
        for item in BANK_LIBRARY.values():
            for kw in item["keywords"]:
                if kw in t:
                    return item["answer"]

    return None

# -----------------------------
# OLLAMA CALL (BANKING ONLY)
# -----------------------------
def call_ollama(prompt):
    try:
        with st.spinner("🤖 BankBot is thinking..."):
            r = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": MODEL_NAME,
                    "prompt": prompt,
                    "stream": False,
                    "options": {
                        "num_predict": 220,
                        "temperature": 0.2
                    }
                },
                timeout=40
            )
        return r.json().get("response", "").strip()
    except Exception:
        return "⚠️ AI service unavailable."


# -----------------------------
# STREAMLIT UI
# -----------------------------
st.set_page_config("BankBot", layout="wide")


st.markdown(
    """
    <style>
    .robot {
        position: fixed;
        bottom: 20px;
        right: 20px;
        width: 120px;
        height: 180px;
        z-index: 9999;
        animation: bounce 1s infinite ease-in-out;
    }

    .head {
        width: 70px;
        height: 50px;
        background: #456232;
        border-radius: 10px;
        margin: auto;
        text-align: center;
        color: white;
        font-size: 24px;
        line-height: 50px;
        animation: headShake 0.5s infinite alternate;
    }

    .body {
        width: 80px;
        height: 60px;
        background: lightgreen;
        margin: 5px auto;
        border-radius: 10px;
    }

    .arms {
        display: flex;
        justify-content: space-between;
        width: 120px;
        margin: auto;
    }

    .arm {
        width: 15px;
        height: 50px;
        background: green;
        animation: armSwing 0.6s infinite alternate;
    }

    .legs {
        
        display: flex;
        justify-content: space-between;
        width: 60px;
        margin: auto;
    }

    .leg {
        width: 15px;
        height: 45px;
        background: #333;
        animation: legDance 0.6s infinite alternate;
    }

    @keyframes bounce {
        0% { transform: translateY(0); }
        50% { transform: translateY(-10px); }
        100% { transform: translateY(0); }
    }

    @keyframes headShake {
        from { transform: rotate(-8deg); }
        to { transform: rotate(8deg); }
    }

    @keyframes armSwing {
        from { transform: rotate(-20deg); }
        to { transform: rotate(20deg); }
    }

    @keyframes legDance {
        from { transform: rotate(10deg); }
        to { transform: rotate(-10deg); }
    }
    </style>

    <div class="robot">
        <div class="head">🤖</div>
        <div class="arms">
            <div class="arm"></div>
            <div class="arm"></div>
        </div>
        <div class="body"></div>
        <div class="legs">
            <div class="leg"></div>
            <div class="leg"></div>
        </div>
    </div>
    """,
    unsafe_allow_html=True
)



st.title("🏦 BankBot – Banking-AI Assistant")

# -----------------------------
# SESSION STATE
# -----------------------------
if "current_chat" not in st.session_state:
    st.session_state.current_chat = []

if "search" not in st.session_state:
    st.session_state.search = ""

# -----------------------------
# SIDEBAR
# -----------------------------
with st.sidebar:
    st.header("🔧 Controls")

    col1, col2 = st.columns(2)

    if col1.button("🆕 New Chat"):
        save_current_chat()
        st.session_state.current_chat = []
        st.success("New chat started")

    if col2.button("🗑️ Clear All"):
        save_all_sessions({"sessions": []})
        st.session_state.current_chat = []
        st.success("All chats deleted")

    st.divider()

    st.subheader("🕘 Previous Chats")
    st.text_input("🔍 Search history", key="search")

    data = load_all_sessions()
    query = st.session_state.search.lower().strip()

    with st.container(height=350):
        if not data["sessions"]:
            st.info("No stored chats")
        else:
            for session in reversed(data["sessions"]):
                for role, msg in session["messages"]:
                    if query and query not in msg.lower():
                        continue
                    st.markdown(f"**{role}:** {msg}")

    st.divider()

    st.subheader("💰 Balance")
    with st.form("bal", clear_on_submit=True):
        a = st.text_input("Account Number")
        p = st.text_input("PIN", type="password")
        if st.form_submit_button("Check"):
            acc = find_account(a)
            if acc and acc["pin"] == p:
                st.success(f"₹{acc['balance']:,.2f}")
            else:
                st.error("Invalid")

    st.divider()

    st.subheader("👤 Account Details")
    with st.form("details", clear_on_submit=True):
        a2 = st.text_input("Account Number")
        p2 = st.text_input("PIN", type="password")
        if st.form_submit_button("Get Details"):
            acc = find_account(a2)
            if acc and acc["pin"] == p2:
                st.json(acc)
            else:
                st.error("Invalid")

# -----------------------------
# MAIN CHAT
# -----------------------------
st.subheader("💬 Current Chat")

for role, msg in st.session_state.current_chat:
    st.markdown(f"**{role}:** {msg}")
    
    




st.divider()

# -----------------------------
# INPUT (FINAL BANKING-ONLY LOGIC)
# -----------------------------
with st.form("chat_form", clear_on_submit=True):
    user_text = st.text_input("Ask a banking question…")
    send = st.form_submit_button("Send")

    if send and user_text.strip():
        st.session_state.current_chat.append(("You", user_text))

        if "pin" in user_text.lower() or "account number" in user_text.lower():
            reply = "🔐 Use sidebar forms for secure banking information."

        else:
            rule_answer = check_bank_library(user_text)

            if rule_answer:
                reply = rule_answer

            elif not is_banking_question(user_text):
                reply = (
                    "❌ I am a banking-only assistant.\n\n"
                    "You can ask about:\n"
                    "- Bank accounts\n"
                    "- Loans & EMI\n"
                    "- Interest rates\n"
                    "- Cards & ATM\n"
                    "- Deposits & KYC"
                )

            else:
                reply = call_ollama(
                    f"{SYSTEM_PROMPT}\nUser: {user_text}\nAssistant:"
                )

        st.session_state.current_chat.append(("Bot", reply))
        st.rerun()

st.caption("✔  Banking-AI Assistantgbvb")
