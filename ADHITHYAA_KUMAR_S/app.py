# app.py - BankBot AI Frontend (UPDATED)
import streamlit as st
import streamlit.components.v1 as components
import requests
import time

st.set_page_config(
    page_title="BankBot AI - Instant Banking Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Modern CSS with loading fixes
st.markdown("""
<style>
    /* Hide Streamlit elements */
    #MainMenu, footer, header {visibility: hidden !important;}
    .stApp, .block-container {padding: 0 !important; margin: 0 !important;}
    
    /* Custom styles */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(10px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    .fade-in { animation: fadeIn 0.3s ease-in; }
    
    /* Better loading indicator */
    @keyframes pulse {
        0% { opacity: 0.6; }
        50% { opacity: 1; }
        100% { opacity: 0.6; }
    }
    
    .loading-pulse {
        animation: pulse 1.5s infinite;
        color: #4CAF50;
        font-weight: bold;
    }
</style>
""", unsafe_allow_html=True)

# Read HTML file
try:
    with open('index.html', 'r', encoding='utf-8') as f:
        html_content = f.read()
    
    # Update all branding to BankBot AI
    html_content = html_content.replace('NEXA BANK', 'BankBot AI')
    html_content = html_content.replace('NEXA Bank AI', 'BankBot AI')
    html_content = html_content.replace('NEXA Bank', 'BankBot AI')
    
    # Add loading indicator to HTML if needed
    if 'loading' not in html_content.lower():
        html_content = html_content.replace('</body>', '''
    <script>
        // Add loading state management
        window.addEventListener('load', function() {
            console.log('BankBot AI Frontend Loaded');
            // Hide any loading indicators
            const loadingEls = document.querySelectorAll('.loading, .typing');
            loadingEls.forEach(el => el.style.display = 'none');
        });
        
        // Auto-retry for failed requests
        let retryCount = 0;
        function retryConnection() {
            if (retryCount < 3) {
                retryCount++;
                console.log('Retrying connection...', retryCount);
                setTimeout(() => {
                    // Trigger a health check
                    fetch('http://localhost:5000/health')
                        .then(response => {
                            if (response.ok) {
                                console.log('Backend reconnected');
                                location.reload();
                            }
                        });
                }, 2000);
            }
        }
    </script>
    </body>
    ''')
    
    # Embed HTML
    components.html(html_content, height=850, scrolling=False)
    
except FileNotFoundError:
    st.error("⚠️ index.html file not found")
    st.info("Make sure index.html is in the same folder as app.py")

# Enhanced Sidebar with better connection management
with st.sidebar:
    st.title("🤖 BankBot AI")
    st.caption("Instant Banking Assistant")
    st.markdown("---")
    
    # Connection Status
    st.subheader("🔌 Connection Status")
    
    status_col1, status_col2 = st.columns(2)
    
    with status_col1:
        if st.button("🔄 Check Health", use_container_width=True, key="health_check"):
            try:
                start = time.time()
                # Use shorter timeout
                response = requests.get("http://localhost:5000/health", timeout=3)
                response_time = round((time.time() - start) * 1000, 2)
                
                if response.status_code == 200:
                    data = response.json()
                    st.success(f"""
✅ **Connected**
Time: {response_time}ms
Cache: {data.get('cache_size', 0)} items
Engine: {data.get('ai_engine', 'v5.0')}
                    """)
                else:
                    st.error("❌ Backend Error")
            except requests.exceptions.ConnectionError:
                st.error("""
🔌 **Backend Offline**
Start backend with:
```bash
cd "your_folder"
python ai_backend.py
```""")
            except requests.exceptions.Timeout:
                st.warning("⏱️ Timeout - Backend slow")
            except Exception as e:
                st.error(f"⚠️ Error: {str(e)[:50]}")
    
    with status_col2:
        if st.button("📊 System Info", use_container_width=True, key="system_info"):
            try:
                response = requests.get("http://localhost:5000/api/system/info", timeout=3)
                if response.status_code == 200:
                    data = response.json()
                    st.success(f"""
**{data['name']}**
Version: {data['version']}
Status: Production Ready
                    """)
                else:
                    st.error("Cannot fetch info")
            except:
                st.error("Service unavailable")
    
    st.markdown("---")
    
    # Performance Monitor
    st.subheader("⚡ Performance")
    
    # Simulated metrics
    metric_col1, metric_col2, metric_col3 = st.columns(3)
    with metric_col1:
        st.metric("Response", "< 2s")
    with metric_col2:
        st.metric("Uptime", "99.9%")
    with metric_col3:
        st.metric("Today", "0")
    
    st.markdown("---")
    
    # Quick Tips
    st.subheader("💡 Quick Tips")
    st.caption("• Use template buttons for instant answers")
    st.caption("• Keep questions specific")
    st.caption("• Contact: 1800-BANKBOT")
    st.caption("• App available on iOS/Android")
    
    # Auto-refresh
    if st.button("🔄 Auto-refresh", key="auto_refresh"):
        st.rerun()

# JavaScript injection for better UX
components.html("""
<script>
// Performance monitoring
const perf = {
    startTime: null,
    markStart: function() {
        this.startTime = Date.now();
        this.showTyping();
    },
    markEnd: function() {
        if (this.startTime) {
            const duration = Date.now() - this.startTime;
            console.log(`BankBot AI: Response in ${duration}ms`);
            this.hideTyping();
        }
    },
    showTyping: function() {
        const chatBox = document.querySelector('.chat-container');
        if (chatBox) {
            const typing = document.createElement('div');
            typing.className = 'typing-indicator loading-pulse';
            typing.id = 'bankbot-typing';
            typing.textContent = 'BankBot AI is responding...';
            chatBox.appendChild(typing);
            chatBox.scrollTop = chatBox.scrollHeight;
        }
    },
    hideTyping: function() {
        const typing = document.getElementById('bankbot-typing');
        if (typing) typing.remove();
    }
};

// Intercept chat messages
document.addEventListener('DOMContentLoaded', function() {
    console.log('BankBot AI Frontend v2.0 Loaded');
    
    // Listen for send events
    const sendBtn = document.querySelector('.send-button, [type="submit"], button');
    if (sendBtn) {
        sendBtn.addEventListener('click', function() {
            perf.markStart();
        });
    }
    
    // Auto-hide loading after 3 seconds (safety)
    setTimeout(() => {
        perf.hideTyping();
    }, 3000);
});
</script>
""", height=0)

# Footer
st.markdown("---")
footer_col1, footer_col2 = st.columns([2, 1])
with footer_col1:
    st.caption("🤖 BankBot AI v5.0 • 🔐 Bank-Grade Security • ⚡ Instant Responses")
with footer_col2:
    st.caption(f"🕐 {time.strftime('%I:%M %p')}")