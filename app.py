import streamlit as st
import pandas as pd
import graphviz
import json
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Corporate Advisory Intelligence", layout="wide")

# =============================
# PREMIUM GLOBAL STYLE
# =============================
st.markdown("""
<style>
.stApp {
    background: linear-gradient(120deg, #141e30, #243b55);
}
.block-container {
    padding: 3rem;
}
h1, h2, h3, p, label {
    color: white !important;
}
.card {
    background: rgba(255,255,255,0.08);
    padding: 30px;
    border-radius: 18px;
    margin-bottom: 25px;
    backdrop-filter: blur(10px);
    box-shadow: 0 8px 32px rgba(0,0,0,0.3);
    animation: fadeIn 0.7s ease;
}
@keyframes fadeIn {
    from {opacity:0; transform: translateY(20px);}
    to {opacity:1; transform: translateY(0);}
}
.metric-card {
    background: linear-gradient(90deg, #00c6ff, #0072ff);
    padding: 25px;
    border-radius: 15px;
    text-align:center;
}
</style>
""", unsafe_allow_html=True)

st.title("Corporate Advisory Intelligence Platform")
st.write("Interactive US Business Structure & Simulation Engine")

# =============================
# NAVIGATION
# =============================
tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Executive Overview",
    "Knowledge Studio",
    "Advisory Lab",
    "Simulation Arena",
    "Intelligence Dashboard"
])

# =============================
# EXECUTIVE OVERVIEW
# =============================
with tab1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Platform Vision")
    st.write("""
    Transforming static legal education into procedural intelligence training.
    • Interactive learning
    • Structured advisory reasoning
    • Simulation-based decision making
    • Measurable advisory intelligence
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# =============================
# KNOWLEDGE STUDIO
# =============================
with tab2:

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Entity Comparison Table")

    data = {
        "Entity": ["C-Corp", "S-Corp", "LLC", "Partnership"],
        "Liability": ["Limited", "Limited", "Limited", "Unlimited (GP)"],
        "Taxation": ["Double", "Pass-through", "Flexible", "Pass-through"],
        "VC Friendly": ["Yes", "No", "Limited", "No"]
    }

    df = pd.DataFrame(data)
    st.dataframe(df)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Entity Selection Flow")

    dot = graphviz.Digraph()
    dot.node("Start", "Start")
    dot.node("Funding", "Seeking VC?")
    dot.node("CCorp", "Choose C-Corp")
    dot.node("Flex", "Need Flexibility?")
    dot.node("LLC", "Choose LLC")
    dot.edges([
        ("Start", "Funding"),
        ("Funding", "CCorp"),
        ("Funding", "Flex"),
        ("Flex", "LLC")
    ])
    st.graphviz_chart(dot)
    st.markdown('</div>', unsafe_allow_html=True)

# =============================
# ADVISORY LAB (Activity 1)
# =============================
with tab3:

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Legal Opinion Drafting – Mark & Bill")

    st.write("""
    Draft a structured legal opinion addressing:
    1. Suitable business model
    2. S-Corp limitations
    3. Taxation comparison
    """)

    opinion = st.text_area("Draft your legal opinion here:", height=250)

    if st.button("Evaluate Opinion"):
        score = 0
        if "liability" in opinion.lower():
            score += 3
        if "tax" in opinion.lower():
            score += 3
        if "corporation" in opinion.lower():
            score += 2
        if "llc" in opinion.lower():
            score += 2

        st.success(f"Preliminary Advisory Score: {score}/10")

    st.markdown('</div>', unsafe_allow_html=True)

# =============================
# SIMULATION ARENA (Activity 2)
# =============================
with tab4:

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Entity Advisory Simulation")

    example = st.selectbox("Select Scenario", [
        "Rishee Tech Startup",
        "LawSikho US Expansion",
        "Single Professional Setup",
        "Priyanka Gadget Expansion",
        "Tara Pet Store"
    ])

    choice = st.selectbox("Recommended Entity",
                          ["C-Corp", "S-Corp", "LLC", "Sole Proprietorship"])

    if st.button("Submit Decision"):
        st.success("Decision recorded for evaluation.")

    st.markdown('</div>', unsafe_allow_html=True)

# =============================
# INTELLIGENCE DASHBOARD
# =============================
with tab5:

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Advisory Intelligence Metrics")

    st.markdown('<div class="metric-card">', unsafe_allow_html=True)
    st.write("Advisory Readiness Index")
    st.write("78 / 100")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
