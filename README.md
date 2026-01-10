# BankBot – Banking FAQ Chatbot 🏦

BankBot is a **secure, domain-restricted banking FAQ chatbot** built using **Streamlit**, **Ollama**, and **Python**. It answers **only banking-related questions** and blocks all unrelated queries.

## 👥 Team Members (Team C)
* **Satyaban Jena**
* **Tejaswini V Gowda**
* **Adhithyaa Kumar S**
* **Nishmitha M C**
* **Jaisurya**
* **Karri Siva Krishna**

---

## 🚀 Features
* **Banking-only FAQ responses**: Specialized knowledge base for banking.
* **Non-banking query restriction**: Safely blocks irrelevant questions.
* **Local LLM using Ollama**: Runs securely on local hardware.
* **Simple Streamlit UI**: User-friendly interface.

## 🛠️ Tech Stack
* **Python**
* **Streamlit** (Frontend)
* **Ollama** (LLM Integration)
* **Custom Filtering Logic**

---

## ⚙️ How It Works
> **User Query** $\rightarrow$ **Banking Filter** $\rightarrow$ **Ollama** $\rightarrow$ **Safe Response**

## 🏃‍♂️ How to Run
To run the application locally, execute the following commands:

```bash
ollama run llama3
streamlit run app.py
