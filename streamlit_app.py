import streamlit as st
import random

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Reddit CyberSafe Game",
    page_icon="🎮",
    layout="centered"
)

# ---------------- SESSION STATE ----------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "name" not in st.session_state:
    st.session_state.name = ""

if "score" not in st.session_state:
    st.session_state.score = 0

# ---------------- LOGIN SCREEN ----------------
if not st.session_state.logged_in:
    st.title("🎮 Reddit CyberSafe Game")
    st.caption("Learn cyber safety while having fun!")
    st.markdown("**Powered by Ebiklean Global**")

    name = st.text_input("Enter your name")

    if st.button("Login"):
        if name.strip() == "":
            st.warning("Please enter your name to continue.")
        else:
            st.session_state.name = name
            st.session_state.logged_in = True
            st.rerun()

# ---------------- MAIN GAME ----------------
else:
    st.sidebar.success(f"Logged in as {st.session_state.name}")
    if st.sidebar.button("Logout"):
        st.session_state.logged_in = False
        st.session_state.score = 0
        st.rerun()

    st.title("🎮 Reddit CyberSafe Game")
    st.markdown("**Powered by Ebiklean Global**")
    
    st.subheader("Instructions")
    st.write(
        "Answer the questions correctly to earn points.\n"
        "Learn cyber safety while having fun!"
    )

    # Sample quiz questions
    questions = [
        {
            "question": "You receive a message from an unknown person asking for your password. What should you do?",
            "options": ["Give your password", "Ignore and report", "Click the link", "Reply politely"],
            "answer": "Ignore and report"
        },
        {
            "question": "You find a USB stick in a public place. What should you do?",
            "options": ["Plug it into your computer", "Hand it to IT/security", "Throw it away", "Keep it"],
            "answer": "Hand it to IT/security"
        },
        {
            "question": "You are using public Wi-Fi. How do you stay safe?",
            "options": ["Use VPN", "Share passwords", "Disable firewall", "None of the above"],
            "answer": "Use VPN"
        },
        {
            "question": "A link in Reddit seems suspicious. What do you do?",
            "options": ["Click immediately", "Check URL carefully", "Share with friends", "Ignore completely"],
            "answer": "Check URL carefully"
        },
    ]

    # Shuffle and pick a random question
    question = random.choice(questions)

    st.write(f"**Question:** {question['question']}")
    user_answer = st.radio("Choose an answer:", question["options"])

    if st.button("Submit Answer"):
        if user_answer == question["answer"]:
            st.success("Correct! ✅")
            st.session_state.score += 10
        else:
            st.error(f"Wrong! ❌ The correct answer is: {question['answer']}")
        
        st.write(f"Your current score: {st.session_state.score}")

        # ---------------- DOWNLOADABLE SCORE REPORT ----------------
        report = f"""
🎮 REDDIT CYBERSAFE GAME REPORT
Powered by Ebiklean Global

Name: {st.session_state.name}
Current Score: {st.session_state.score}

Keep learning cyber safety to protect yourself online!
"""

        st.download_button(
            label="📥 Download Your Score Report",
            data=report,
            file_name="reddit_cybersafe_score.txt",
            mime="text/plain"
        )

    st.divider()
    st.subheader("💰 Investor & Impact Overview")
    st.write(
        """
        - Gamified learning improves engagement  
        - Raises awareness about phishing and online safety  
        - Scalable for schools, NGOs, Reddit communities  
        """
    )
