# test_gemini_2.5_flash.py
import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()

api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("❌ ERROR: No API key found in .env file!")
    print("Add: GEMINI_API_KEY=your_real_key_here")
    exit(1)

# Mask the key for safe display
if api_key and len(api_key) > 14:
    masked_key = f"{api_key[:10]}...{api_key[-4:]}"
    print(f"API Key (masked): {masked_key}")
else:
    print("❌ ERROR: API key format looks invalid")

# Test URL for Gemini 2.5 Flash
url = f"https://generativelanguage.googleapis.com/v1/models/gemini-2.5-flash:generateContent"

payload = {
    "contents": [{
        "parts": [{"text": "Say hello in one word"}]
    }],
    "generationConfig": {
        "maxOutputTokens": 20,
        "temperature": 0.7
    }
}

headers = {
    "Content-Type": "application/json"
}

print("\n" + "=" * 70)
print("🔍 TESTING GEMINI 2.5 FLASH MODEL")
print("=" * 70)
print(f"URL: {url}")
print(f"Model: gemini-2.5-flash")

try:
    print("\n📤 Sending request...")
    response = requests.post(
        f"{url}?key={api_key}",
        json=payload,
        headers=headers,
        timeout=15
    )
    
    print(f"📥 Response Status: {response.status_code}")
    
    if response.status_code == 200:
        data = response.json()
        print("✅ SUCCESS! Model is working!")
        print("\n📋 Response Details:")
        
        if 'candidates' in data and len(data['candidates']) > 0:
            candidate = data['candidates'][0]
            text = candidate['content']['parts'][0]['text']
            print(f"🤖 AI Response: {text}")
            
            # Check for token usage info
            if 'usageMetadata' in candidate:
                usage = candidate['usageMetadata']
                print(f"🔢 Token Usage:")
                print(f"   Prompt tokens: {usage.get('promptTokenCount', 'N/A')}")
                print(f"   Candidates tokens: {usage.get('candidatesTokenCount', 'N/A')}")
                print(f"   Total tokens: {usage.get('totalTokenCount', 'N/A')}")
        
        # Show full response structure
        print("\n📊 Response Structure:")
        print(json.dumps(data, indent=2)[:500] + "...")
        
    elif response.status_code == 404:
        print("❌ ERROR 404: Model not found!")
        print("\n💡 Possible reasons:")
        print("1. Model name is incorrect")
        print("2. Model is not available in your region")
        print("3. Model requires special access (might be in preview)")
        print("4. Try different model names:")
        print("   - gemini-2.0-flash-exp")
        print("   - gemini-1.5-flash-latest")
        print("   - gemini-1.5-pro-latest")
        
    elif response.status_code == 403:
        print("❌ ERROR 403: Permission denied!")
        print("\n💡 Possible reasons:")
        print("1. API key is invalid or expired")
        print("2. API key doesn't have access to this model")
        print("3. Billing not set up or quota exceeded")
        
    elif response.status_code == 400:
        print("❌ ERROR 400: Bad Request")
        print(f"\nResponse: {response.text[:200]}")
        
    elif response.status_code == 429:
        print("⚠️  ERROR 429: Rate limit exceeded")
        print("Try again in a few minutes")
        
    else:
        print(f"❌ Unexpected error: {response.status_code}")
        print(f"Response: {response.text[:200]}")
        
except requests.exceptions.Timeout:
    print("❌ Request timeout - Try increasing timeout value")
except requests.exceptions.ConnectionError:
    print("❌ Connection error - Check internet connection")
except Exception as e:
    print(f"❌ Unexpected error: {e}")

# Also test for model availability
print("\n" + "=" * 70)
print("🔍 CHECKING MODEL AVAILABILITY")
print("=" * 70)

def check_model(model_name):
    """Check if a model is available"""
    check_url = f"https://generativelanguage.googleapis.com/v1/models/{model_name}"
    
    try:
        response = requests.get(f"{check_url}?key={api_key}", timeout=5)
        if response.status_code == 200:
            return True, "✅ Available"
        elif response.status_code == 404:
            return False, "❌ Not found"
        else:
            return False, f"❌ Error {response.status_code}"
    except:
        return False, "❌ Connection failed"

# Check various model names
models_to_check = [
    "gemini-2.5-flash",
    "gemini-2.0-flash-exp",
    "gemini-1.5-flash-latest",
    "gemini-1.5-pro-latest",
    "gemini-1.0-pro-latest",
]

for model in models_to_check:
    available, message = check_model(model)
    print(f"{model:30} {message}")