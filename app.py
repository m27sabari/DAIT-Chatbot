import streamlit as st
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="DAIT Assistant",
    page_icon="🎓",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
body {
    background-image: url("https://images.unsplash.com/photo-1524995997946-a1c2e315a42f");
    background-size: cover;
    background-attachment: fixed;
}

.stApp {
    backdrop-filter: blur(4px); /* 25% blur */
    background-color: rgba(0, 0, 0, 0.25);
}

.chat-box {
    background-color: rgba(255,255,255,0.92);
    padding: 10px;
    border-radius: 10px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown(
    "<h1 style='text-align:center;'>🎓 DAIT Assistant</h1>",
    unsafe_allow_html=True
)

st.markdown(
    "<p style='text-align:center;'>Your friendly college buddy 😄</p>",
    unsafe_allow_html=True
)

# ---------------- SESSION STATE ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "name" not in st.session_state:
    st.session_state.name = None

# ---------------- HELPER FUNCTION ----------------
def bot_reply(user_msg):
    msg = user_msg.lower()

    if st.session_state.name is None:
        st.session_state.name = user_msg.strip()
        return f"Nice to meet you, **{st.session_state.name}** 😄  
How can I help you today?"

    if "hello" in msg or "hi" in msg:
        return random.choice([
            f"Hey {st.session_state.name}! 👋",
            f"Hello {st.session_state.name}! 😊",
            f"Hi buddy 😄 What’s up?"
        ])

    if "college" in msg or "dait" in msg:
        return (
            "🏫 **Dhaanish Ahmed Institute of Technology (DAIT)** is located in Coimbatore.\n\n"
            "• AICTE approved\n"
            "• Anna University affiliated\n"
            "• Strong focus on Engineering & Technology\n\n"
            "Want details about departments, admissions or placements? 😉"
        )

    if "course" in msg or "department" in msg:
        return (
            "📚 DAIT offers:\n"
            "• CSE\n"
            "• AI & DS\n"
            "• ECE\n"
            "• Mechanical\n"
            "• Civil\n\n"
            "Which department are you interested in?"
        )

    if "placement" in msg:
        return (
            "💼 DAIT provides placement training, internships, and industry exposure.\n\n"
            "Skills + confidence = Success 🚀"
        )

    if "bye" in msg:
        return f"Bye {st.session_state.name}! 👋  
Come back anytime 😄"

    return random.choice([
        "Hmm 🤔 tell me more!",
        "Interesting 😄 go on...",
        "I’m listening 👂",
        "That sounds cool!"
    ])

# ---------------- CHAT DISPLAY ----------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------------- USER INPUT ----------------
user_input = st.chat_input(
    "Type your message here..." if st.session_state.name else "Hey! What's your name? 😊"
)

if user_input:
    # Show user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    with st.chat_message("user"):
        st.markdown(user_input)

    # Bot response
    reply = bot_reply(user_input)

    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })

    with st.chat_message("assistant"):
        st.markdown(reply)
