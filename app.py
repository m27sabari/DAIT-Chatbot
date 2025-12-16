import streamlit as st
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="DAIT Assistant",
    page_icon="🎓",
    layout="wide"
)

# ---------------- BACKGROUND & STYLE ----------------
st.markdown("""
<style>
.stApp {
    background-image: url("https://images.unsplash.com/photo-1524995997946-a1c2e315a42f");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
    backdrop-filter: blur(4px); /* 25% blur */
}

.chat-box {
    background-color: rgba(255, 255, 255, 0.92);
    padding: 12px;
    border-radius: 12px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- TITLE ----------------
st.markdown("<h1 style='text-align:center;'>🎓 DAIT Assistant</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center;'>Your friendly college buddy 😄</p>", unsafe_allow_html=True)

# ---------------- SESSION STATE ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

if "name" not in st.session_state:
    st.session_state.name = None

# ---------------- BOT LOGIC ----------------
def bot_reply(user_msg):
    msg = user_msg.lower()

    # Ask name first
    if st.session_state.name is None:
        st.session_state.name = user_msg.strip()
        return f"Nice to meet you, {st.session_state.name}! 😄 How can I help you today?"

    # Greetings
    if "hello" in msg or "hi" in msg:
        return random.choice([
            f"Hey {st.session_state.name}! 👋",
            f"Hello {st.session_state.name}! 😊",
            "Hi there! How’s your day going? 😄"
        ])

    # College info
    if "college" in msg or "dait" in msg:
        return (
            "🏫 **Dhaanish Ahmed Institute of Technology (DAIT)** is located in Coimbatore.\n\n"
            "• AICTE Approved\n"
            "• Anna University Affiliated\n"
            "• Excellent learning environment\n\n"
            "Want to know about courses, placements or hostels? 😉"
        )

    # Courses
    if "course" in msg or "department" in msg:
        return (
            "📚 **Courses Offered at DAIT:**\n"
            "• CSE\n"
            "• AI & DS\n"
            "• ECE\n"
            "• Mechanical\n"
            "• Civil\n\n"
            "Which department are you interested in?"
        )

    # Placements
    if "placement" in msg:
        return (
            "💼 DAIT focuses on placements with:\n"
            "• Training programs\n"
            "• Internship support\n"
            "• Industry exposure\n\n"
            "Skills + Confidence = Success 🚀"
        )

    # Bye
    if "bye" in msg:
        return f"Bye {st.session_state.name}! 👋 Come back anytime 😄"

    # Default
    return random.choice([
        "Hmm 🤔 tell me more!",
        "Interesting 😄 go on...",
        "I’m listening 👂",
        "That sounds cool!"
    ])

# ---------------- DISPLAY CHAT ----------------
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# ---------------- USER INPUT ----------------
prompt = "Hey! What's your name? 😊" if st.session_state.name is None else "Type your message here..."
user_input = st.chat_input(prompt)

if user_input:
    # Store user message
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
