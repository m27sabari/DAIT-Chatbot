import streamlit as st
import base64

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="DAIT College Assistant",
    page_icon="🎓",
    layout="centered"
)

# ------------------ BACKGROUND IMAGE ------------------
def set_background(image_file):
    with open(image_file, "rb") as f:
        encoded = base64.b64encode(f.read()).decode()

    css = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{encoded}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}
    .chat-box {{
        background-color: rgba(255, 255, 255, 0.6);
        padding: 20px;
        border-radius: 12px;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

set_background("background.jpg")

# ------------------ COLLEGE DATA ------------------
college_info = {
    "name": "Dhaanish Ahmed Institute of Technology (DAIT)",
    "location": "Coimbatore, Tamil Nadu",
    "type": "Private Engineering College",
    "courses": "B.E, B.Tech, M.E",
    "departments": "CSE, AI&DS, ECE, EEE, Mechanical, Civil",
    "facilities": "Library, Hostel, Transport, Labs, Sports, Canteen",
    "placements": "Training & Placement Cell with good placement support",
    "hostel": "Separate hostels for boys and girls",
    "library": "Well-equipped digital library",
    "contact": "https://dhaanish.com"
}

college_keywords = [
    "college", "dait", "course", "department", "placement",
    "hostel", "library", "facility", "admission", "location"
]

# ------------------ CHATBOT LOGIC ------------------
def chatbot_reply(user_input):
    text = user_input.lower()

    # Greetings
    if text in ["hi", "hello", "hey", "hai"]:
        return "😊 Hello! Welcome to **DAIT College Assistant**. How can I help you today?"

    # Name
    if "name" in text:
        return f"Our college name is **{college_info['name']}** 🎓"

    if "location" in text:
        return f"📍 DAIT is located in **{college_info['location']}**."

    if "course" in text or "degree" in text:
        return f"📘 Courses offered: **{college_info['courses']}**"

    if "department" in text:
        return f"🏫 Departments: **{college_info['departments']}**"

    if "placement" in text:
        return f"💼 Placements: {college_info['placements']}"

    if "hostel" in text:
        return f"🏠 Hostel: {college_info['hostel']}"

    if "library" in text:
        return f"📚 Library: {college_info['library']}"

    if "facility" in text:
        return f"🏀 Facilities: {college_info['facilities']}"

    # Check if college-related keyword exists
    for word in college_keywords:
        if word in text:
            return "ℹ️ Please ask clearly about **DAIT College**."

    # Not related to college
    return "❌ I can answer only **college-related questions**. Please ask about **DAIT College**."

# ------------------ UI ------------------
st.markdown("<div class='chat-box'>", unsafe_allow_html=True)

st.title("🎓 DAIT College Assistant")
st.caption("Ask anything about Dhaanish Ahmed Institute of Technology")

if "messages" not in st.session_state:
    st.session_state.messages = []

for role, msg in st.session_state.messages:
    st.chat_message(role).write(msg)

user_input = st.chat_input("Type your question about DAIT...")

if user_input:
    st.session_state.messages.append(("user", user_input))
    reply = chatbot_reply(user_input)
    st.session_state.messages.append(("assistant", reply))

    st.chat_message("user").write(user_input)
    st.chat_message("assistant").write(reply)

st.markdown("</div>", unsafe_allow_html=True)
