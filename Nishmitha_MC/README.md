🤖BankBot AI – Banking FAQ Chatbot

BankBot AI is a banking-domain specific chatbot built using Streamlit and Ollama (LLaMA3).
It strictly answers only banking and finance-related questions and blocks all non-banking queries.


📌 Features

 ➤Interactive chat interface using Streamlit

 ➤Answers only banking & finance-related queries

 ➤Automatically blocks non-banking questions

 ➤Powered by LLaMA3 via Ollama
 

📂Chat history management:

⇨Multiple saved chats

⇨Auto-generated chat titles

⇨Create & delete chats


🛠️ Tech Stack

→ Python

→ Streamlit

→ Ollama (LLaMA3)

→ Custom banking query validation logic


📂 Project Structure
├── Bot.py

├── banking_intellect.py

├── README.md


⚙️ Installation & Setup
1️⃣Install dependencies
pip install streamlit ollama

2️⃣Run Ollama (LLaMA3)
ollama run llama3

3️⃣Start the application
streamlit run Bot.py

