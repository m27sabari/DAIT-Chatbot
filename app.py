import streamlit as st
import random

# -------- PAGE CONFIG --------
st.set_page_config(
    page_title="DAIT College Assistant",
    page_icon="🎓",
    layout="wide"
)

# -------- BACKGROUND + CSS --------
st.markdown("""
<style>
.stApp {
    background-image: url("background.jpg");  /* your background image */
    background-size: cover;
    background-repeat: no-repeat;
    background-position: center;
}

.block-container {
    backdrop-filter: blur(2px);
    background-color: rgba(255,255,255,0.6);  /* ~60% visible */
    border-radius: 15px;
    padding: 15px;
}

.stChatMessage.assistant {
    background: #6a11cb;
    color: white;
    padding: 12px;
    border-radius: 15px;
}

.stChatMessage.user {
    background: #00c6ff;
    color: white;
    padding: 12px;
    border-radius: 15px;
    text-align: right;
}
</style>
""", unsafe_allow_html=True)

st.title("🎓 DAIT College Assistant")
st.markdown("Ask me anything about **Dhaanish Ahmed Institute of Technology (DAIT)**!")

# -------- KNOWLEDGE BASE --------
knowledge = {
    "about": (
        "🏫 Dhaanish Ahmed Institute of Technology (DAIT) is an engineering college "
        "located in Veerappanur, K.G.Chavadi, Coimbatore-641105, Tamil Nadu, India. "
        "It was established in 2013, is AICTE-approved, and affiliated with Anna University, Chennai."
    ),
    "location": "📍 DAIT is located at Veerappanur, K.G.Chavadi, Coimbatore-641105, Tamil Nadu, India.",
    "courses": (
        "📚 DAIT offers B.E/B.Tech programs including:\n"
        "• Computer Science & Engineering (CSE)\n"
        "• AI & Data Science\n"
        "• Artificial Intelligence & Machine Learning\n"
        "• Cyber Security\n"
        "• Robotics & Automation\n"
        "• Biomedical Engineering\n"
        "• Electronics & Communication Engineering\n"
        "• Information Technology\n"
        "• Food Technology"
    ),
    "departments": (
        "Departments include CSE, AI & DS, ECE, EEE, Biomedical, Cyber Security, "
        "Robotics & Automation, IT, and Food Technology."
    ),
    "hostel": (
        "🏠 DAIT has separate hostel facilities for boys and girls with Wi-Fi, "
        "comfortable rooms, mess, and recreational areas."
    ),
    "placement": (
        "💼 The placement cell at DAIT provides training, soft skills, interview "
        "preparation, and placement support. Recruiters include Infosys, Amazon, IBM, "
        "Cognizant etc., with packages up to ~25 LPA previously."
    ),
    "library": "📚 DAIT has a central library with books, digital resources, and study spaces.",
    "facilities": (
        "🏫 Facilities include smart classrooms, labs, library, sports grounds, "
        "cafeteria, transport, and medical support."
    ),
    "admission": (
        "🎓 Admissions are based on 10+2 (Physics, Chemistry, Maths) eligibility "
        "through TNEA counseling or merit."
    ),
    "contact": (
        "☎️ Contact DAIT:\n"
        "• Phone: +91-422-7172060\n"
        "• Admissions: +91-9176786000\n"
        "• Website: https://dhaanish.com/"
    ),
    "timing": "🕘 College working hours are generally from 9:00 AM to 4:30 PM."
}

# -------- KEYWORD LISTS (for matching) --------
college_keywords = [
    "about", "location", "courses", "department", "hostel",
    "placement", "library", "facilities", "admission",
    "contact", "timing", "college", "dait"
]

greetings = ["hello", "hi", "hey", "how are you", "good morning", "good afternoon", "good evening"]

# -------- SESSION STATE --------
if "messages" not in st.session_state:
    st.session_state.messages = []

# -------- DISPLAY CHAT --------
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_input = st.chat_input("Type your message...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    text = user_input.lower().strip()
    reply = ""

    # Friendly greeting
    for g in greetings:
        if g in text:
            reply = random.choice([
                "Hey there! 😊 Ask me anything about DAIT College!",
                "Hi! 👋 How can I help you with DAIT today?",
                "Hello! 😄 Interested in DAIT details?"
            ])
            break

    # Check if college related
    if reply == "":
        matched = False
        for key in college_keywords:
            if key in text:
                reply = knowledge.get(key, "")
                matched = True
                break

        if not matched:
            reply = (
                "Sorry, I can help only with questions about DAIT College 😊. "
                "Please ask me about admissions, courses, hostel, placements, facilities, location etc."
            )

    st.session_state.messages.append({"role": "assistant", "content": reply})

    st.experimental_rerun()
