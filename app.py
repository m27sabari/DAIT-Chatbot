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
    "college name": "Dhaanish Ahmed Institute of Technology (DAIT)",
    "who are you": "I an your DAIT assistant,How can i help you ?",
    "fees","fee":"The fee structure varies by course and is as per Anna University and Management norms,so kindly contact our admission cell.",
    "join": "you can join in our college by Government Quata and Management Quata.",
    "discipline","rules": "The college follows strict discipline to ensure a safe and focused learning environment",
    "ragging" : "The campus follows a zero-tolerance anti-ragging policy",
    "medical facilities" : "Basic medical and first-aid facilities are avilabe on campus, We have focused on our students Health",
    "Reachcollege" : "First you come to Coimbatore Gandhipuram or Ukkadam Bus stand and here always bus no:96 or bus no:48 are availabe,you can reach the college by bus no:96 and 48.",
    "scholarship": "Government and management scholarships are available for eligible students",
    "eligiblity": "Candidates must have completed higher secondary education or Diplamo with  required subjects as per Anna Univercity",
    "location": "KG Chavadi, Coimbatore, Tamil Nadu",
    "type": "Private Engineering College",
    "courses": "B.E, B.Tech",
    "departments": "CSE, AI&DS, ECE, AI&ML, BME, R&A, FOOD TECH, IT",
    "facilities": "Library, Hostel, Transport, Labs, Sports, Canteen",
    "placements": "Training & Placement Cell with good placement support",
    "hostel": "Separate hostels for boys and girls with Good WIFI facilities",
    "library": "Well-equipped digital library",
    "contact": "students can contact the college thruogh phone,email,or official website: https://dhaanish.com"
}

college_keywords = [
    "college name", " "dait", "course", "department", "placement",
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
