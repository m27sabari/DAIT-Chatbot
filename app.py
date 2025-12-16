import streamlit as st
import base64
import random

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="DAIT College Assistant",
    page_icon="🎓",
    layout="wide"
)

# ---------- LOAD BACKGROUND IMAGE ----------
def set_bg(image_file):
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
            background-color: rgba(255, 255, 255, 0.6);
            padding: 20px;
            border-radius: 15px;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

# SET BACKGROUND
set_bg("bg.jpg")

# ---------- TITLE ----------
st.markdown(
    "<h1 style='text-align:center;'>🎓 DAIT College Assistant</h1>",
    unsafe_allow_html=True
)
st.markdown(
    "<p style='text-align:center;'>Ask anything about Dhaanish Ahmed Institute of Technology</p>",
    unsafe_allow_html=True
)

# ---------- COLLEGE DATA ----------
college_data = {
    "about": "Dhaanish Ahmed Institute of Technology (DAIT) is an engineering college located in Coimbatore, Tamil Nadu. Established in 2013, it is AICTE approved and affiliated to Anna University.",
    "location": "DAIT is located at Veerappanur, K.G. Chavadi, Coimbatore – 641105.",
    "courses": "Courses offered include CSE, AI & DS, AIML, Cyber Security, ECE, IT, Biomedical Engineering, Robotics & Automation, and Food Technology.",
    "hostel": "DAIT provides separate hostel facilities for boys and girls with food, Wi-Fi, and security.",
    "placement": "DAIT has an active placement cell with training programs. Students are placed in companies like Infosys, Cognizant, IBM, Amazon, etc.",
    "facilities": "Facilities include smart classrooms, laboratories, library, transport, sports ground, cafeteria, and medical support.",
    "admission": "Admissions are through TNEA counseling or management quota based on eligibility.",
    "contact": "Website: https://dhaanish.com | Phone: +91 9176786000"
}

college_keywords = college_data.keys()

greetings = ["hi", "hello", "hey", "how are you", "good morning", "good evening"]

# ---------- CHAT MEMORY ----------
if "chat" not in st.session_state:
    st.session_state.chat = []

# ---------- DISPLAY CHAT ----------
for msg in st.session_state.chat:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------- USER INPUT ----------
user_input = st.chat_input("Type your message here...")

if user_input:
    st.session_state.chat.append({"role": "user", "content": user_input})

    text = user_input.lower()
    response = ""

    # Greeting response
    if any(greet in text for greet in greetings):
        response = random.choice([
            "Hello! 😊 Welcome to DAIT College Assistant.",
            "Hi there! 👋 How can I help you about DAIT?",
            "Hey! 😄 Ask me anything about DAIT College."
        ])
    else:
        found = False
        for key in college_keywords:
            if key in text:
                response = college_data[key]
                found = True
                break

        if not found:
            response = (
                "❗ I can help only with **DAIT College related questions**.\n\n"
                "Please ask about courses, hostel, placements, facilities, admission, etc."
            )

    st.session_state.chat.append({"role": "assistant", "content": response})
