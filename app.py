import streamlit as st
import base64
import os

# ------------------ PAGE CONFIG ------------------
st.set_page_config(
    page_title="DAIT College Assistant",
    page_icon="🎓",
    layout="centered"
)

# ------------------ BACKGROUND IMAGE ------------------
def set_background(image_file):
    if not os.path.exists(image_file):
        st.warning("Background image not found. App loaded without background.")
        return

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
        background-color: rgba(255, 255, 255, 0.7);
        padding: 20px;
        border-radius: 12px;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

set_background("background.jpg")

# ------------------ COLLEGE DATA ------------------
college_info = {
    "college_name": "Dhaanish Ahmed Institute of Technology (DAIT)",
    "assistant": "I am your DAIT College Assistant. How can I help you?",
    "fees": "Fee structure varies by course. Please contact the admission office.",
    "admission": "Admissions are through Government Quota and Management Quota.",
    "discipline": "Strict discipline is maintained for a safe learning environment.",
    "ragging": "Zero-tolerance anti-ragging policy is followed.",
    "medical": "Basic medical and first-aid facilities are available on campus.",
    "reach": "From Coimbatore Gandhipuram or Ukkadam bus stand, take bus No. 96 or 48.",
    "scholarship": "Government and management scholarships are available.",
    "eligibility": "12th or Diploma with required subjects as per Anna University norms.",
    "location": "KG Chavadi, Coimbatore, Tamil Nadu",
    "type": "Private Engineering College",
    "courses": "B.E, B.Tech",
    "departments": "CSE, AI&DS, ECE, AI&ML, BME, Robotics & Automation, Food Technology, IT",
    "facilities": "Library, Hostel, Transport, Labs, Sports, Canteen",
    "placements": "Dedicated Training & Placement Cell with good placement support",
    "hostel": "Separate hostels for boys and girls with WiFi",
    "library": "Well-equipped digital library",
    "contact": "Website: https://dhaanish.com | Phone & Email available on official site"
}

# ------------------ CHATBOT LOGIC ------------------
def chatbot_reply(user_input):
    text = user_input.lower()

    if text in ["hi", "hello", "hey", "hai"]:
        return "😊 Hello! Welcome to **DAIT College Assistant**. How can I help you?"

    if "who are you" in text:
        return college_info["assistant"]

    if "college name" in text or "dait" in text:
        return f"🎓 **{college_info['college_name']}**"

    if "location" in text:
        return f"📍 Location: {college_info['location']}"

    if "course" in text or "degree" in text:
        return f"📘 Courses Offered: {college_info['courses']}"

    if "department" in text:
        return f"🏫 Departments: {college_info['departments']}"

    if "placement" in text:
        return f"💼 Placements: {college_info['placements']}"

    if "hostel" in text:
        return f"🏠 Hostel: {college_info['hostel']}"

    if "library" in text:
        return f"📚 Library: {college_info['library']}"

    if "facility" in text:
        return f"🏀 Facilities: {college_info['facilities']}"

    if "fee" in text:
        return f"💰 Fees: {college_info['fees']}"

    if "admission" in text or "join" in text:
        return f"📝 Admission: {college_info['admission']}"

    if "scholarship" in text:
        return f"🎓 Scholarship: {college_info['scholarship']}"

    if "contact" in text:
        return f"📞 Contact: {college_info['contact']}"

    return "❌ I can answer only **DAIT College-related questions**."

# ------------------ UI ------------------
st.markdown("<div class='chat-box'>", unsafe_allow_html=True)

st.title("🎓 DAIT College Assistant")
st.caption("Ask anything about Dhaanish Ahmed Institute of Technology")

if "messages" not in st.session_state:
    st.session_state.messages = []

for role, msg in st.session_state.messages:
    st.chat_message(role).write(msg)

user_input = st.chat_input("Ask your question about DAIT...")

if user_input:
    st.session_state.messages.append(("user", user_input))
    reply = chatbot_reply(user_input)
    st.session_state.messages.append(("assistant", reply))

    st.chat_message("user").write(user_input)
    st.chat_message("assistant").write(reply)

st.markdown("</div>", unsafe_allow_html=True)
