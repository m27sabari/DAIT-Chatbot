import streamlit as st

# ---------------- PAGE SETUP ----------------
st.set_page_config(page_title="DAIT College Chatbot", page_icon="🎓")

st.title("🎓 DAIT College Chatbot")
st.caption("Dhaanish Ahmed Institute of Technology – College Information Assistant")

# ---------------- KNOWLEDGE BASE ----------------
college_info = {
    "about": "Dhaanish Ahmed Institute of Technology (DAIT) is an engineering college located in Coimbatore, Tamil Nadu. It was established in 2013, approved by AICTE and affiliated with Anna University, Chennai.",

    "location": "DAIT is located at Veerappanur, K.G. Chavadi, Coimbatore – 641105, Tamil Nadu.",

    "courses": (
        "DAIT offers the following UG courses:\n"
        "- B.E Computer Science and Engineering\n"
        "- B.E CSE (AI & ML)\n"
        "- B.E Cyber Security\n"
        "- B.E Electronics and Communication Engineering\n"
        "- B.E Biomedical Engineering\n"
        "- B.E Robotics and Automation\n"
        "- B.Tech Artificial Intelligence & Data Science\n"
        "- B.Tech Food Technology\n"
        "- B.Tech Information Technology"
    ),

    "admission": (
        "Admissions are based on 10+2 (Physics, Chemistry, Mathematics). "
        "Students can apply through TNEA counselling or college admission office.\n"
        "Admission Contact: +91 91767 86000"
    ),

    "hostel": (
        "DAIT provides separate hostel facilities for boys and girls. "
        "Both AC and Non-AC rooms are available with good food, security and play areas."
    ),

    "placement": (
        "DAIT has a Training and Placement Cell which provides:\n"
        "- Soft skill training\n"
        "- Aptitude training\n"
        "- Internship and placement support"
    ),

    "contact": (
        "Phone: 0422-7172060\n"
        "Admission: +91 91767 86000\n"
        "Website: https://dhaanish.com"
    )
}

college_keywords = [
    "college", "dait", "dhaanish", "course", "department", "admission",
    "hostel", "placement", "fee", "contact", "location", "address"
]

# ---------------- CHAT HISTORY ----------------
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat history
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# ---------------- CHAT INPUT ----------------
user_input = st.chat_input("Ask me about DAIT College...")

if user_input:
    # Show user message
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.markdown(user_input)

    user_text = user_input.lower()
    reply = ""

    # ---------------- RULE-BASED LOGIC ----------------
    if "about" in user_text or "college" in user_text:
        reply = college_info["about"]

    elif "location" in user_text or "address" in user_text:
        reply = college_info["location"]

    elif "course" in user_text or "department" in user_text:
        reply = college_info["courses"]

    elif "admission" in user_text or "apply" in user_text:
        reply = college_info["admission"]

    elif "hostel" in user_text:
        reply = college_info["hostel"]

    elif "placement" in user_text or "job" in user_text:
        reply = college_info["placement"]

    elif "contact" in user_text or "phone" in user_text:
        reply = college_info["contact"]

    # ❌ NON-COLLEGE QUESTIONS
    elif not any(word in user_text for word in college_keywords):
        reply = (
            "❌ I can help only with **DAIT College related questions**.\n\n"
            "Please ask about:\n"
            "- Courses\n"
            "- Admissions\n"
            "- Hostels\n"
            "- Placements\n"
            "- Location or Contact details"
        )

    else:
        reply = "Please ask a clear question related to DAIT College."

    # Show bot reply
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)
