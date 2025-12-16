import streamlit as st
import random
import base64
from datetime import datetime

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="DAIT Assistant",
    page_icon="🎓",
    layout="wide"
)

# ---------------- BACKGROUND ----------------
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
            background-attachment: fixed;
        }}

        .block-container {{
            padding-top: 1rem;
        }}

        .stChatMessage {{
            background: rgba(0,0,0,0.6);
            border-radius: 12px;
            padding: 12px;
            color: white;
        }}

        h1, h3, h4, p, span {{
            color: white !important;
            text-shadow: 1px 1px 3px black;
        }}
        </style>
        """,
        unsafe_allow_html=True
    )

set_background("background.jpg")  # put image in same folder

# ---------------- HEADER ----------------
st.markdown("<h1>🎓 DAIT Assistant</h1>", unsafe_allow_html=True)
st.markdown("<h4>Dhaanish Ahmed Institute of Technology, Coimbatore</h4>", unsafe_allow_html=True)
st.markdown("---")

# ---------------- TIME GREETING ----------------
hour = datetime.now().hour
if hour < 12:
    greet = "Good Morning ☀️"
elif hour < 18:
    greet = "Good Afternoon 🌤️"
else:
    greet = "Good Evening 🌙"

# ---------------- KNOWLEDGE BASE ----------------
college_info = {
    "about": [
        "about", "college", "dait", "institute"
    ],
    "location": [
        "location", "where", "place", "address"
    ],
    "courses": [
        "courses", "departments", "branch", "degree"
    ],
    "hostel": [
        "hostel", "stay", "accommodation"
    ],
    "placement": [
        "placement", "job", "company", "career"
    ],
    "facilities": [
        "facilities", "library", "lab", "sports"
    ],
    "admission": [
        "admission", "join", "apply"
    ],
    "timing": [
        "timing", "college time", "working hours"
    ]
}

answers = {
    "about": "Dhaanish Ahmed Institute of Technology (DAIT) is an engineering college in Coimbatore, Tamil Nadu.",
    "location": "DAIT is located in Coimbatore, Tamil Nadu.",
    "courses": "DAIT offers B.E / B.Tech programs like CSE, AI & DS, ECE, EEE and Mechanical Engineering.",
    "hostel": "DAIT provides separate hostel facilities for boys and girls.",
    "placement": "The placement cell supports students with training and job opportunities.",
    "facilities": "Facilities include smart classrooms, labs, library, sports, cafeteria and transport.",
    "admission": "Admissions are done through counseling based on eligibility.",
    "timing": "College working hours are generally from 9:00 AM to 4:30 PM."
}

greetings = ["hi", "hello", "hey", "good morning", "good evening"]

# ---------------- SESSION STATE ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# ---------------- INITIAL MESSAGE ----------------
if len(st.session_state.messages) == 0:
    st.session_state.messages.append({
        "role": "assistant",
        "content": f"{greet} 😊\n\nI am the **DAIT Assistant**.\nAsk me anything about the college."
    })

# ---------------- DISPLAY CHAT ----------------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# ---------------- QUICK BUTTONS (FIXED) ----------------
st.markdown("### 🔘 Quick Questions")
cols = st.columns(5)
buttons = ["Courses", "Hostel", "Placement", "Facilities", "Location"]

for i, btn in enumerate(buttons):
    with cols[i]:
        if st.button(btn, key=btn):
            st.session_state.messages.append({
                "role": "user",
                "content": btn.lower()
            })
            st.experimental_rerun()

# ---------------- USER INPUT ----------------
user_input = st.chat_input("Ask about DAIT college...")

if user_input:
    user_text = user_input.lower()
    st.session_state.messages.append({"role": "user", "content": user_input})

    reply = None

    # Greeting check
    if any(greet in user_text for greet in greetings):
        reply = random.choice([
            "Hello 😊 How can I help you about DAIT?",
            "Hi there! Ask me anything about DAIT 🎓",
            "Hey! I’m here to help you with college info 👍"
        ])

    # College intent check
    if reply is None:
        for key, keywords in college_info.items():
            if any(word in user_text for word in keywords):
                reply = answers[key]
                break

    # Not college related
    if reply is None:
        reply = (
            "I can help only with **DAIT college information** 😊\n"
            "Please ask about courses, hostel, placement, facilities or admission."
        )

    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.experimental_rerun()
