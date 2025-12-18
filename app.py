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
        background-color: rgba(255, 255, 255, 0.8);
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
    "assistant": "I am your DAIT College Assistant. I support English, Tamil, and Malayalam. How can I help you?",

    "location": "Dhaanish Avenue, Veerappanur, K.G. Chavadi, Coimbatore – 641105, Tamil Nadu",
    "type": "Private Engineering College affiliated to Anna University and approved by AICTE",

    "courses": "B.E / B.Tech – CSE, AI & DS, AI & ML, ECE, IT, Biomedical Engineering, Robotics & Automation, Food Technology",
    "pg_courses": "M.E, MBA, MCA (subject to availability)",
    "duration": "B.E / B.Tech courses are 4 years in duration",

    "eligibility": "10+2 with Physics, Chemistry, and Mathematics as per Anna University norms. Lateral entry for diploma holders.",
    "admission": "Admissions through TNEA counseling and Management Quota.",
    "documents": "10th & 12th mark sheets, Transfer Certificate, Community Certificate, Aadhar ID, passport-size photos.",

    "fees": "Fee structure varies by course and quota. Please contact the Admission Office.",
    "scholarship": "Government and management merit-based scholarships available.",

    "departments": "CSE, AI & DS, AI & ML, ECE, IT, Biomedical Engineering, Robotics & Automation, Food Technology",

    "attendance": "Minimum 75% attendance is mandatory as per Anna University norms.",
    "exam_rules": "All examinations are conducted as per Anna University regulations.",

    "placements": "Dedicated Training & Placement Cell with strong industry support.",
    "packages": "Highest package: 25 LPA | Average package: 9 LPA",
    "companies": (
        "Major recruiters include Wipro, Hexaware, TCS, Zoho, Emerson, Quest Global, "
        "Tech Mahindra, Cognizant (CTS), Avasoft, Apollo Tyres. "
        "Industry collaborations with Bosch, Renault Nissan, and Ashok Leyland."
    ),

    "internship": "Internship and industrial training opportunities are provided through the placement cell.",

    "facilities": "Library, Hostels, Transport, Laboratories, Sports, Auditorium, Canteen, Wi-Fi Campus",
    "hostel": "Separate hostels for boys and girls with Wi-Fi and security",
    "library": "Well-equipped central and digital library",
    "transport": "College bus facility from major locations in Coimbatore",
    "medical": "On-campus first-aid facility with quick access to nearby hospitals",

    "events": "Technical symposiums, cultural programs, NSS activities, workshops, and annual fests",

    "bonafide": "Bonafide and Transfer Certificates can be applied through the College Office (Information Center – IC).",

    "grievance": (
        "DAIT has a Student Grievance Redressal Committee (SGRC). "
        "Complaints can be submitted via the college website portal, "
        "email: antiraggingcell@dhaanishcollege.in, "
        "or helpline numbers: 83449 16000 / 86000 58000."
    ),

    "portal": "Student Portal (ERP) and Learning Management System (LMS) are available for students.",

    "discipline": "Strict discipline is maintained to ensure a safe and professional environment.",
    "ragging": "Zero-tolerance anti-ragging policy is strictly followed.",

    "reach": "From Gandhipuram or Ukkadam Bus Stand, take Bus No. 96 or 48 towards K.G. Chavadi.",

    "contact": "Website: https://dhaanish.com | Phone & email details are available on the official website."
}

# ------------------ CHATBOT LOGIC ------------------
def chatbot_reply(user_input):
    text = user_input.lower()

    if text in ["hi", "hello", "hey", "hai"]:
        return "😊 Hello! Welcome to **DAIT College Assistant**."

    if "who are you" in text or "assistant" in text:
        return college_info["assistant"]

    if "college name" in text:
        return f"🎓 {college_info['college_name']}"

    if "location" in text or "where" in text:
        return f"📍 {college_info['location']}"

    if "affiliated" in text or "aicte" in text:
        return f"🏛️ {college_info['type']}"

    if "course" in text or "degree" in text:
        return f"📘 {college_info['courses']}"

    if "pg" in text:
        return f"🎓 {college_info['pg_courses']}"

    if "duration" in text:
        return f"⏳ {college_info['duration']}"

    if "admission" in text or "apply" in text:
        return f"📝 {college_info['admission']}"

    if "eligibility" in text:
        return f"🧑‍🎓 {college_info['eligibility']}"

    if "document" in text:
        return f"📄 {college_info['documents']}"

    if "fee" in text:
        return f"💰 {college_info['fees']}"

    if "scholarship" in text:
        return f"🎓 {college_info['scholarship']}"

    if "department" in text or "branch" in text:
        return f"🏫 {college_info['departments']}"

    if "attendance" in text:
        return f"📊 {college_info['attendance']}"

    if "exam" in text:
        return f"📝 {college_info['exam_rules']}"

    if "placement" in text:
        return f"💼 {college_info['placements']}\n📦 {college_info['packages']}"

    if "company" in text or "recruiter" in text:
        return f"🏢 {college_info['companies']}"

    if "internship" in text:
        return f"🧑‍💻 {college_info['internship']}"

    if "facility" in text:
        return f"🏀 {college_info['facilities']}"

    if "hostel" in text:
        return f"🏠 {college_info['hostel']}"

    if "library" in text:
        return f"📚 {college_info['library']}"

    if "transport" in text or "bus" in text:
        return f"🚌 {college_info['transport']}"

    if "medical" in text:
        return f"🏥 {college_info['medical']}"

    if "event" in text or "fest" in text:
        return f"🎉 {college_info['events']}"

    if "bonafide" in text or "tc" in text:
        return f"📑 {college_info['bonafide']}"

    if "grievance" in text or "complaint" in text:
        return f"⚖️ {college_info['grievance']}"

    if "portal" in text or "lms" in text:
        return f"💻 {college_info['portal']}"

    if "ragging" in text:
        return f"🚫 {college_info['ragging']}"

    if "discipline" in text or "rule" in text:
        return f"🧑‍💼 {college_info['discipline']}"

    if "contact" in text:
        return f"📞 {college_info['contact']}"

    if "reach" in text:
        return f"📍 {college_info['reach']}"

    return "❌ Please ask questions related to **DAIT College** only."

# ------------------ UI ------------------
st.markdown("<div class='chat-box'>", unsafe_allow_html=True)
st.title("🎓 DAIT College Assistant")
st.caption("Official College Website Chatbot")

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
