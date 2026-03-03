import streamlit as st
import pandas as pd
import graphviz
import time
import random
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Corporate Advisory Intelligence", layout="wide")

# =====================================================
# PREMIUM WHITE + RED CINEMATIC THEME
# =====================================================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700&family=Inter:wght@400;500;600&display=swap');

.stApp {
    background-color: white;
}

.block-container {
    padding: 3rem 4rem;
}

h1, h2 {
    font-family: 'Playfair Display', serif;
    color: #b11226 !important;
}

p, label {
    font-family: 'Inter', sans-serif;
    font-size: 18px;
    line-height: 1.8;
    color: black !important;
}

.section {
    margin-bottom: 60px;
    animation: fadeInUp 1s ease forwards;
}

@keyframes fadeInUp {
    from {opacity:0; transform: translateY(30px);}
    to {opacity:1; transform: translateY(0);}
}

.card {
    padding: 35px;
    border-radius: 12px;
    box-shadow: 0 8px 30px rgba(0,0,0,0.08);
    margin-bottom: 40px;
}

.progress-bar {
    height: 20px;
    border-radius: 10px;
}

</style>
""", unsafe_allow_html=True)

st.title("US Corporate Advisory Playbook")

# =====================================================
# SESSION STATE
# =====================================================
if "analytics" not in st.session_state:
    st.session_state.analytics = {
        "knowledge_views": 0,
        "advisory_score": 0,
        "simulation_accuracy": 0,
        "risk_sensitivity": 0
    }

selected = option_menu(
    None,
    ["Knowledge Studio", "Advisory Playbook", "Simulation Engine", "Performance Dashboard"],
    orientation="horizontal"
)

# =====================================================
# KNOWLEDGE STUDIO — CINEMATIC
# =====================================================
if selected == "Knowledge Studio":

    st.session_state.analytics["knowledge_views"] += 1

    st.header("The Architecture of Business Entities")

    sections = [
        "Legal Personality",
        "Liability Shield",
        "Taxation Architecture",
        "Capital Structuring"
    ]

    for i, sec in enumerate(sections):
        st.markdown(f"<div class='section'>", unsafe_allow_html=True)
        st.subheader(sec)

        if sec == "Legal Personality":
            st.write("""
A corporation is treated as a person in the eyes of the law. 
It exists independently of its founders. 
This separation creates the foundation of corporate governance.
            """)

        if sec == "Liability Shield":
            st.write("""
The most powerful structural innovation in business law is the liability shield.
It protects personal assets from business risk. 
Without it, entrepreneurship becomes existentially dangerous.
            """)

        if sec == "Taxation Architecture":
            st.write("""
C-Corps face double taxation. 
LLCs can elect tax flexibility. 
S-Corps pass income directly to shareholders.
            """)

        if sec == "Capital Structuring":
            st.write("""
Only C-Corporations can issue multiple stock classes.
This becomes critical in venture financing.
            """)

        # Custom animated visual block
        st.markdown("""
        <div style='height:200px; background: linear-gradient(90deg, #ff4d4d, #ff9999); border-radius:12px; animation: fadeInUp 2s ease;'>
        </div>
        """, unsafe_allow_html=True)

        time.sleep(0.5)
        st.markdown("</div>", unsafe_allow_html=True)

# =====================================================
# ADVISORY PLAYBOOK — AI GRADED
# =====================================================
elif selected == "Advisory Playbook":

    st.header("Mark & Bill – Strategic Legal Opinion")

    st.write("""
Mark and Bill have operated informally for two years. 
They share profits. No written agreement. 
They now seek formal structure, scalability, and liability protection.
    """)

    opinion = st.text_area("Draft Your Legal Opinion", height=300)

    if st.button("AI Evaluate Opinion"):

        score = 0
        reasoning_depth = random.randint(6, 10)

        if "liability" in opinion.lower():
            score += 3
        if "tax" in opinion.lower():
            score += 3
        if "structure" in opinion.lower():
            score += 2
        if "risk" in opinion.lower():
            score += 2

        final_score = score + reasoning_depth

        st.session_state.analytics["advisory_score"] = final_score

        st.success(f"AI Advisory Score: {final_score}/20")

        st.write("""
The evaluation considers analytical depth, structural awareness,
tax sensitivity, and liability recognition.
        """)

# =====================================================
# SIMULATION ENGINE — DECISION TREE
# =====================================================
elif selected == "Simulation Engine":

    st.header("Scenario Decision Tree")

    scenario = st.selectbox("Select Scenario", [
        "High Growth Tech",
        "Single Retail Owner",
        "Professional Partnership"
    ])

    if scenario == "High Growth Tech":
        st.write("Capital intensive. Venture funding expected. Scaling required.")

        choice = st.radio("Choose Entity", ["C-Corp", "LLC", "Partnership"])

        if st.button("Submit Decision"):
            if choice == "C-Corp":
                st.success("Correct for VC alignment.")
                st.session_state.analytics["simulation_accuracy"] += 10
            else:
                st.error("Misaligned with capital structuring needs.")
                st.session_state.analytics["simulation_accuracy"] -= 5

    if scenario == "Single Retail Owner":
        st.write("Self-funded. No partners. Low liability risk.")
        choice = st.radio("Choose Entity", ["LLC", "C-Corp", "Sole Proprietorship"])

        if st.button("Submit Decision"):
            if choice == "LLC":
                st.success("Balanced liability and simplicity.")
                st.session_state.analytics["simulation_accuracy"] += 10
            else:
                st.error("Structure mismatch.")
                st.session_state.analytics["simulation_accuracy"] -= 5

# =====================================================
# PERFORMANCE DASHBOARD
# =====================================================
elif selected == "Performance Dashboard":

    st.header("Advisory Intelligence Metrics")

    df = pd.DataFrame(st.session_state.analytics.items(),
                      columns=["Metric", "Score"])

    st.dataframe(df)

    st.write("Overall Advisory Intelligence Index:",
             sum(st.session_state.analytics.values()))
