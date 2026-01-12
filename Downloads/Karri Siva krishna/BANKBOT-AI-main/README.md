# 🤖 BANK BOT AI

A production-ready, fully-customizable AI banking chatbot built with pure HTML, CSS, and JavaScript. Designed for seamless integration into financial applications, BANK BOT AI delivers secure, intelligent banking support powered by local LLMs through Ollama.

## 🚀 Quick Start

### Prerequisites
- [Ollama](https://ollama.ai/) installed and running locally
- Python 3.7+ with Streamlit
- Modern web browser

### Installation & Setup

```bash
# Clone the repository
git clone https://github.com/yourusername/bank-bot-ai.git
cd bank-bot-ai

# Install Python dependencies
pip install -r requirements.txt

# Start Ollama with your preferred model
ollama run llama3

# Launch BANK BOT AI
streamlit run app.py
```

## 📁 Project Structure

```
bank-bot-ai/
├── index.html              # Main HTML interface
├── style.css               # All CSS styling (banking themes, responsive design)
├── script.js               # Core JavaScript logic (chat, templates, Ollama calls)
├── app.py                  # Streamlit integration and embedding
├── ai_backend.py           # Python backend for Ollama AI integration
├── requirements.txt        # Python dependencies
├── Calculator.class        # Utility class for financial calculations
├── README.md               # This documentation
└── .gitignore              # Git ignore file
```

## 🔧 File Breakdown

| File | Purpose | Key Features |
|------|---------|--------------|
| **`index.html`** | Main UI structure | Chat interface, sidebar, banking templates, responsive layout |
| **`style.css`** | Complete styling | Dark/light banking themes, animations, mobile responsiveness |
| **`script.js`** | Frontend logic | Chat management, Ollama API calls, template system, local storage |
| **`app.py`** | Streamlit wrapper | Embeds HTML in Streamlit, hides UI elements, performance monitor |
| **`ai_backend.py`** | AI integration | Ollama connection handler, model management, response processing |
| **`requirements.txt`** | Dependencies | Streamlit, requests, other Python requirements |
| **`Calculator.class`** | Financial utilities | Banking calculations, interest computations, transaction math |

## 🏦 Key Features

### **🎯 Banking-Specific Chat**
- **Smart Banking Templates**: One-click queries for balance, transfers, loans, statements
- **Financial Advice**: Personalized banking guidance powered by local LLMs
- **Secure Design**: Banking-grade UI with encryption indicators and trust badges

### **🤖 AI Integration**
- **Local LLM Support**: Runs completely offline with Ollama (Llama3, Mistral, Gemma)
- **Multi-Model Switching**: Choose between different AI models for different tasks
- **Context-Aware Responses**: Maintains conversation context for natural interactions

### **💻 Technical Features**
- **Pure Frontend**: No frameworks - just HTML, CSS, JavaScript
- **Streamlit Embedding**: Easy integration into existing Streamlit applications
- **Responsive Design**: Works perfectly on desktop, tablet, and mobile
- **Theme Switching**: Professional dark/light banking modes

### **📊 User Experience**
- **Chat History**: All conversations saved locally and accessible in sidebar
- **Quick Actions**: Banking templates for common financial queries
- **Code Highlighting**: Syntax-highlighted code in responses
- **Real-Time Updates**: Smooth animations and instant message display

## 🚀 Getting Started

### 1. **Basic Setup**
```bash
# 1. Install Ollama (if not already installed)
# Visit https://ollama.ai/ and download for your OS

# 2. Pull and run an AI model
ollama pull llama3
ollama run llama3

# 3. Install Python dependencies
pip install -r requirements.txt

# 4. Launch the application
streamlit run app.py
```

### 2. **Customization**
```css
/* In style.css - Customize banking colors */
:root {
    --banking-primary: #0a1929;
    --banking-accent: #00a86b;
    --banking-gradient: linear-gradient(135deg, #0066cc, #0099ff);
}
```

```javascript
// In script.js - Modify banking templates
const BANKING_TEMPLATES = {
    balance: "Check my account balance",
    transfer: "How do I transfer money?",
    loan: "What are current loan rates?",
    statement: "Get my account statement"
};
```

## 🔌 API Integration

### Ollama Connection
```python
# ai_backend.py handles all Ollama communication
import requests

class OllamaHandler:
    def get_response(self, message, model="llama3"):
        # Sends user message to local Ollama instance
        # Returns AI-generated banking response
```

### Streamlit Embedding
```python
# app.py - Main Streamlit application
import streamlit.components.v1 as components

# Read and embed the HTML interface
with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()
    
components.html(html_content, height=800, scrolling=False)
```

## 🎯 Use Cases

### **For Financial Institutions**
- **24/7 Customer Support**: Automated banking assistance
- **Internal Training Tool**: Staff protocol guidance
- **Demo Platform**: Showcase digital banking capabilities
- **Prototype Testing**: Rapid banking application development

### **For Developers**
- **Learning Resource**: Study AI-chatbot integration patterns
- **Template Foundation**: Customizable base for financial apps
- **Local AI Demo**: Experiment with Ollama LLMs offline
- **Streamlit Integration**: Example of HTML embedding in Streamlit

### **For End Users**
- **Personal Banking Assistant**: Private financial guidance
- **Financial Education**: Learn banking concepts interactively
- **Transaction Practice**: Safe simulation of banking operations
- **Local Privacy**: No data sent to external servers

## 🛠️ Development

### Adding New Features
1. **New Banking Template**:
   - Add to `BANKING_TEMPLATES` in `script.js`
   - Create corresponding button in `index.html`
   - Update system prompt in `ai_backend.py` if needed

2. **New UI Component**:
   - Add HTML structure to `index.html`
   - Style in `style.css`
   - Add interactivity in `script.js`

3. **New AI Model**:
   - Ensure model is available in Ollama
   - Add option to model selector in `index.html`
   - Update model handling in `ai_backend.py`

### Building and Testing
```bash
# Run locally for development
python -m http.server 8000  # For HTML/CSS/JS testing
streamlit run app.py        # For full Streamlit testing

# Check Ollama connection
curl http://localhost:11434/api/tags
```

## 📊 Performance Optimization

| Area | Optimization | Impact |
|------|-------------|--------|
| **Frontend** | Minified CSS/JS, optimized images | Faster load times |
| **AI Responses** | Response caching, template pre-processing | Reduced Ollama calls |
| **Memory** | Efficient chat history management | Lower browser memory usage |
| **Network** | Local Ollama eliminates API calls | Zero latency from external APIs |

## 🤝 Contributing

We welcome contributions! Please:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Contribution Guidelines
- Follow existing code style and structure
- Add comments for complex logic
- Update documentation when adding features
- Test changes thoroughly before submitting

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

## 🏆 Acknowledgments

- **Ollama** for making local LLMs accessible
- **Streamlit** for seamless web app framework
- **Font Awesome** for banking icons
- **Highlight.js** for code syntax highlighting

---

<div align="center">
  
**⭐ If you find BANK BOT AI useful, please give it a star!**

*Built with ❤️ for the financial technology communit*

[Report Bug](https://github.com/yourusername/bank-bot-ai/issues) · [Request Feature](https://github.com/yourusername/bank-bot-ai/issues)

</div>
