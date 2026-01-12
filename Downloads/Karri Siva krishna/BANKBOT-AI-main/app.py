# app.py
import streamlit as st
import streamlit.components.v1 as components
import requests
import time

st.set_page_config(
    page_title="NEXA BANK AI - Banking Assistant",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide all Streamlit UI elements
st.markdown("""
<style>
    #MainMenu {visibility: hidden !important;}
    footer {visibility: hidden !important;}
    header {visibility: hidden !important;}
    
    .stApp {
        padding: 0 !important;
        margin: 0 !important;
        width: 100% !important;
        max-width: 100% !important;
    }
    
    .block-container {
        padding: 0 !important;
        margin: 0 !important;
        width: 100% !important;
        max-width: 100% !important;
    }
    
    .st-emotion-cache-1dp5vir {
        display: none !important;
    }
</style>
""", unsafe_allow_html=True)

# Read the HTML file
with open('index.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Embed the HTML with proper height
components.html(html_content, height=800, scrolling=False)

# Performance monitoring sidebar
with st.sidebar:
    st.title("🏦 NEXA BANK")
    st.subheader("Performance Monitor")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("📊 Health Check", key="health_check"):
            try:
                start = time.time()
                response = requests.get("http://localhost:5000/api/health", timeout=5)
                ping_time = (time.time() - start) * 1000
                
                if response.status_code == 200:
                    data = response.json()
                    st.success(f"✅ Online - {data['ping_ms']}ms")
                else:
                    st.error("❌ Backend Error")
            except:
                st.error("🔌 Backend Offline")
    
    with col2:
        if st.button("⚙️ System Info", key="system_info"):
            try:
                response = requests.get("http://localhost:5000/api/system/info", timeout=5)
                if response.status_code == 200:
                    data = response.json()
                    st.success(f"✅ {data['name']} v{data['version']}")
            except:
                st.error("Cannot fetch system info")