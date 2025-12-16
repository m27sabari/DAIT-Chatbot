import streamlit as st
import random
import base64

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="DAIT College Assistant",
    page_icon="🎓",
    layout="wide"
)

# ---------------- BACKGROUND FUNCTION ----------------
def set_background(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url("data:image/jpg;base64,{encoded}");
            background-size: cover;
            background-position: center;
            background-repeat: no-repeat;
        }}

        .block-container {{
            background-color: rgba(255, 255, 255, 0.6); /* 60% visible */
            padding: 20px;
            border-radius: 15px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# ✅ SET BACKGROUND
set_background("background.jpg")

# ---------------- TITLE ----------------
st.title("🎓 DAIT College Assistant")
st.write("Ask me anything about **Dhaanish Ahmed Institute of Technology (DAIT)**")

# ---------------- KNOWLEDGE BASE ----------------
college_info = {
    "about": "Dhaanish Ahmed Institute of Technology (DAIT) is located in Coimbatore, Tamil Nadu. It is AICTE approved and affiliated to Anna University.",
    "location": "DAIT is located at Veerappanur, K.G.Chavadi, Coimbatore – 641105.",
    "courses": "Courses include CSE, AI & DS, AIML, Cyber Security, Robotics, Biomedical, ECE, IT, and Food Technology.",
    "hostel": "DAIT provides separate hostel facilities for boys and girls with good amenities.",
    "placement": "DAIT has a placement cell that trains students and supports placements in reputed companies.",
    "library": "DAIT has a central library with books, journals, and digital resources.",
    "facilities": "Facilities include smart classrooms, labs, sports grounds, cafeteria, transport, and medical care.",
    "admission": "Admissions are based on eligibility through TNEA counseling and merit.",
    "contact": "Official website: https://dhaanish.com | Phone: +91 9176786000",
}

college_keywords = list(college_info.keys())

greetings = ["hi", "hello", "hey", "how are you", "good morning", "good evening"]

# ---------------- SESSION ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- DISPLAY CHAT ----------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------- USER INPUT ----------------
user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    text = user_input.lower()
    reply = ""

    # Friendly greeting
    if any(greet in text for greet in greetings):
        reply = random.choice([
            "Hello! 😊 Welcome to DAIT College Assistant!",
            "Hi there! 👋 How can I help you about DAIT?",
            "Hey! 😄 Ask me anything about DAIT College."
        ])
    else:
        found = False
        for key in college_keywords:
            if key in text:
                reply = college_info[key]
                found = True
                break

        if not found:
            reply = (
                "❗ I can answer only questions related to **DAIT College**.\n\n"
                "Please ask about courses, hostel, placements, admissions, facilities, etc."
            )

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.rerun()
