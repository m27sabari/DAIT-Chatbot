import streamlit as st
from openai import OpenAI

# ---------------- CONFIG ----------------
st.set_page_config(
    page_title="DAIT Assistant",
    page_icon="🎓",
    layout="wide"
)

import os
from openai import OpenAI

client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

# ---------------- BACKGROUND ----------------
st.markdown("""
<style>
.stApp {
    background-image: url("https://images.unsplash.com/photo-1523050854058-8df90110c9f1");
    background-size: cover;
    background-position: center;
}
.chat-box {
    background: rgba(255,255,255,0.75);
    backdrop-filter: blur(5px);
    padding: 15px;
    border-radius: 15px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown("<h1 style='text-align:center;'>🎓 DAIT Assistant</h1>", unsafe_allow_html=True)

# ---------------- SESSION ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []
    st.session_state.user_name = None

# ---------------- CHAT DISPLAY ----------------
with st.container():
    for msg in st.session_state.messages:
        role = "🧑‍🎓 You" if msg["role"] == "user" else "🤖 DAIT Assistant"
        st.markdown(f"""
        <div class="chat-box">
        <b>{role}:</b><br>{msg["content"]}
        </div><br>
        """, unsafe_allow_html=True)

# ---------------- INPUT ----------------
user_input = st.chat_input("Type your message here...")

# ---------------- LOGIC ----------------
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    if st.session_state.user_name is None:
        st.session_state.user_name = user_input.strip()
        bot_reply = f"Nice to meet you, {st.session_state.user_name}! 😄 How can I help you today?"
    else:
        system_prompt = f"""
You are DAIT Assistant, a funny, friendly, human-like AI.
You help students of Dhaanish Ahmed Institute of Technology.
Talk casually, warmly, and clearly.
User name: {st.session_state.user_name}
"""

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                *st.session_state.messages
            ]
        )

        bot_reply = response.choices[0].message.content

    st.session_state.messages.append({"role": "assistant", "content": bot_reply})
    st.rerun()
