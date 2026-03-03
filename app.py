import streamlit as st
import pandas as pd
import random
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")

# ============================================================
# PREMIUM DESIGN SYSTEM
# ============================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@400;500;600&display=swap');

.stApp { background-color: white; }

.block-container { padding: 2rem 5rem; }

h1, h2, h3 {
    font-family: 'Playfair Display', serif;
    color: #1a237e !important;
}

p {
    font-family: 'Inter', sans-serif;
    font-size: 18px;
    line-height: 1.9;
    color: #111 !important;
}

.section-card {
    padding: 35px;
    border-radius: 16px;
    box-shadow: 0 10px 40px rgba(0,0,0,0.05);
    margin-bottom: 40px;
    animation: fadeIn 0.8s ease;
}

@keyframes fadeIn {
    from {opacity:0; transform: translateY(30px);}
    to {opacity:1; transform: translateY(0);}
}

.chapter-header {
    border-left: 6px solid #f9a825;
    padding-left: 15px;
}

.progress-ring {
    height: 180px;
    width: 180px;
    border-radius: 50%;
    background: conic-gradient(#1a237e var(--percent), #eee 0);
    display:flex;
    align-items:center;
    justify-content:center;
    font-weight:bold;
    font-size:22px;
    color:#1a237e;
}
</style>
""", unsafe_allow_html=True)

# ============================================================
# STATE
# ============================================================
if "completed_chapters" not in st.session_state:
    st.session_state.completed_chapters = []
if "quiz_score" not in st.session_state:
    st.session_state.quiz_score = 0
if "quiz_total" not in st.session_state:
    st.session_state.quiz_total = 0

selected = option_menu(
    None,
    ["Knowledge Studio", "Assessment", "Progress Intelligence"],
    orientation="horizontal"
)

# ============================================================
# KNOWLEDGE STUDIO
# ============================================================
if selected == "Knowledge Studio":

    chapters = {
        "Form 1040 Architecture": """
Form 1040 is not merely a form; it is the structural culmination of all income reporting.
It acts as a master summary. Schedules such as Schedule 1, 2, 3, A, B, C, D, E, F and H
feed into this central document.

Gross income begins with wages (Form W-2), interest (Schedule B),
dividends, IRA distributions, pensions, Social Security,
capital gains (Schedule D), and additional income via Schedule 1.
""",

        "Accounting Period & Methods": """
An accounting period defines the time frame in which income is measured.
Individuals typically use a calendar year.
Businesses may adopt fiscal years.

Under the cash method, income is reported when received.
Under accrual, income is reported when earned.
Hybrid methods blend both approaches.
""",

        "FICA & Self Employment Tax": """
FICA funds Social Security and Medicare.
Employees pay 7.65%, employers match it.

Self-employed individuals pay 15.3%.
However, the IRS allows deduction of the employer-equivalent half.
This is why net earnings are multiplied by 92.35%.
"""
    }

    chapter = st.selectbox("Select Chapter", list(chapters.keys()))

    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.markdown(f"<div class='chapter-header'><h2>{chapter}</h2></div>", unsafe_allow_html=True)

    st.write(chapters[chapter])

    st.image("https://images.unsplash.com/photo-1454165804606-c3d57bc86b40",
             use_column_width=True)

    if st.button("Mark Chapter Complete"):
        if chapter not in st.session_state.completed_chapters:
            st.session_state.completed_chapters.append(chapter)

    st.markdown("</div>", unsafe_allow_html=True)

# ============================================================
# ASSESSMENT
# ============================================================
elif selected == "Assessment":

    questions = [
        {
            "q": "Which income is always taxable?",
            "options": ["Municipal bond interest",
                        "Child support",
                        "Tips reported to employer",
                        "Life insurance proceeds"],
            "answer": "Tips reported to employer",
            "explanation": "Tips are taxable income."
        },
        {
            "q": "Which interest is federally tax-exempt?",
            "options": ["Corporate bond",
                        "Bank savings",
                        "Treasury bond",
                        "Municipal bond"],
            "answer": "Municipal bond",
            "explanation": "Municipal bonds are generally federally tax exempt."
        }
    ]

    for q in questions:
        st.markdown("<div class='section-card'>", unsafe_allow_html=True)
        st.subheader(q["q"])
        choice = st.radio("", q["options"], key=q["q"])

        if st.button("Submit", key=q["q"]+"submit"):
            st.session_state.quiz_total += 1
            if choice == q["answer"]:
                st.success("Correct")
                st.session_state.quiz_score += 1
            else:
                st.error("Incorrect")

            st.info(q["explanation"])

        st.markdown("</div>", unsafe_allow_html=True)

# ============================================================
# PROGRESS INTELLIGENCE
# ============================================================
elif selected == "Progress Intelligence":

    total_chapters = 3
    chapter_completion = len(st.session_state.completed_chapters)
    percent = int((chapter_completion / total_chapters) * 100)

    st.markdown("<div class='section-card'>", unsafe_allow_html=True)
    st.subheader("Learning Progress")

    st.markdown(
        f"<div class='progress-ring' style='--percent:{percent}%;'>{percent}%</div>",
        unsafe_allow_html=True
    )

    st.write(f"Chapters Completed: {chapter_completion} / {total_chapters}")
    st.write(f"Quiz Accuracy: {st.session_state.quiz_score} / {st.session_state.quiz_total}")

    st.subheader("AI Generated Feedback")

    if percent > 70:
        st.success("You demonstrate strong conceptual clarity in income recognition.")
    elif percent > 30:
        st.warning("You understand foundations but require deeper reinforcement.")
    else:
        st.error("Significant revision recommended before advisory application.")

    st.markdown("</div>", unsafe_allow_html=True)
