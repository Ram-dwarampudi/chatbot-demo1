import streamlit as st
import requests

# Replace this with your actual Gemini API key
API_KEY = "AIzaSyAs_8O8KsaBCo9s0W0zj0PiwAftzjKM6wM"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key={API_KEY}"

st.set_page_config(page_title="Gemini Chatbot", page_icon="🤖")
st.title("🤖 Gemini Chatbot")
st.markdown("Ask me anything!")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

# Chat display
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# User input
user_input = st.chat_input("Say something...")

if user_input:
    # Add user message to session
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    # Prepare request to Gemini API
    payload = {
        "contents": [
            {
                "parts": [
                    {"text": user_input}
                ]
            }
        ]
    }

    headers = {
        "Content-Type": "application/json"
    }

    # API call
    response = requests.post(API_URL, headers=headers, json=payload)
    if response.status_code == 200:
        data = response.json()
        bot_reply = data["candidates"][0]["content"]["parts"][0]["text"]
    else:
        bot_reply = "❌ Error: Failed to get response from Gemini API."

    # Add bot message to session
    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    with st.chat_message("assistant"):
        st.markdown(bot_reply)
