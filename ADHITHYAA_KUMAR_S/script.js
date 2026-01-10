// Minimal script.js - Only contains essential functions
document.addEventListener('DOMContentLoaded', function() {
    console.log('Chat UI loaded');
    
    // Auto-resize textarea
    const messageInput = document.getElementById('message-input');
    if (messageInput) {
        messageInput.addEventListener('input', function() {
            this.style.height = 'auto';
            this.style.height = this.scrollHeight + 'px';
        });
    }
    
    // Settings modal toggle
    const settingsBtn = document.getElementById('settings-btn');
    const closeSettings = document.getElementById('close-settings');
    const settingsModal = document.getElementById('settings-modal');
    
    if (settingsBtn && settingsModal) {
        settingsBtn.addEventListener('click', () => {
            settingsModal.classList.add('active');
        });
    }
    
    if (closeSettings && settingsModal) {
        closeSettings.addEventListener('click', () => {
            settingsModal.classList.remove('active');
        });
    }
    
    // Theme toggle
    const themeToggle = document.getElementById('theme-toggle');
    if (themeToggle) {
        themeToggle.addEventListener('click', function() {
            const body = document.body;
            if (body.classList.contains('dark-mode')) {
                body.classList.remove('dark-mode');
                body.classList.add('light-mode');
                this.querySelector('span').textContent = 'Light Mode';
                this.querySelector('i').className = 'fas fa-sun';
            } else {
                body.classList.remove('light-mode');
                body.classList.add('dark-mode');
                this.querySelector('span').textContent = 'Dark Mode';
                this.querySelector('i').className = 'fas fa-moon';
            }
        });
    }
});