import streamlit as st
import os
from openai import OpenAI

# Page config
st.set_page_config(
    page_title="DAIT Assistant",
    page_icon="🎓",
    layout="wide"
)

# Background image + blur control
st.markdown("""
<style>
.stApp {
    background-image: url("https://images.unsplash.com/photo-1523050854058-8df90110c9f1");
    background-size: cover;
    background-position: center;
}
.chat-container {
    backdrop-filter: blur(4px);
    background: rgba(0,0,0,0.55);
    padding: 20px;
    border-radius: 15px;
}
</style>
""", unsafe_allow_html=True)

# OpenAI client
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

# Session state
if "messages" not in st.session_state:
    st.session_state.messages = []
if "name" not in st.session_state:
    st.session_state.name = None

st.title("🎓 DAIT Assistant")

with st.container():
    st.markdown('<div class="chat-container">', unsafe_allow_html=True)

    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    user_input = st.chat_input("Type your message...")

    if user_input:
        st.session_state.messages.append(
            {"role": "user", "content": user_input}
        )

        with st.chat_message("assistant"):
            if st.session_state.name is None:
                st.session_state.name = user_input.strip()
                reply = f"Nice to meet you, **{st.session_state.name}** 😄  
I’m your friendly **DAIT Assistant** 🎓  
Ask me anything about the college, courses, campus life or just chat!"
            else:
                system_prompt = f"""
You are DAIT Assistant.
You talk friendly, funny, polite and human-like.
You help students of Dhaanish Ahmed Institute of Technology.
Use simple English, emojis sometimes, and sound natural.
User name: {st.session_state.name}
"""

                response = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=[
                        {"role": "system", "content": system_prompt},
                        *st.session_state.messages
                    ],
                    temperature=0.7
                )

                reply = response.choices[0].message.content

            st.markdown(reply)
            st.session_state.messages.append(
                {"role": "assistant", "content": reply}
            )

    st.markdown("</div>", unsafe_allow_html=True)
