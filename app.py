import streamlit as st
import pandas as pd
import graphviz
import time

st.set_page_config(page_title="Corporate Advisory Intelligence", layout="wide")

# ==========================
# WHITE + RED THEME
# ==========================
st.markdown("""
<style>
.stApp {
    background-color: white;
}
.block-container {
    padding: 3rem;
}
h1, h2, h3 {
    color: #b11226 !important;
}
p, label {
    color: #333333 !important;
}
.card {
    background: #ffffff;
    padding: 30px;
    border-radius: 12px;
    margin-bottom: 25px;
    box-shadow: 0 8px 25px rgba(0,0,0,0.08);
    animation: fadeIn 0.6s ease;
}
@keyframes fadeIn {
    from {opacity:0; transform: translateY(15px);}
    to {opacity:1; transform: translateY(0);}
}
.red-btn > button {
    background-color: #b11226;
    color: white;
    border-radius: 8px;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

st.title("Corporate Advisory Intelligence Platform")
st.markdown("Transforming US Business Law into Procedural Intelligence")

tab1, tab2, tab3, tab4 = st.tabs([
    "Executive Overview",
    "Knowledge Studio",
    "Advisory Lab",
    "Simulation Arena"
])

# =====================================================
# EXECUTIVE OVERVIEW
# =====================================================
with tab1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Platform Objective")

    st.write("""
    This platform converts theoretical understanding of US business entities into:
    • Structured analytical reasoning  
    • Real-world advisory application  
    • Simulation-based intelligence testing  
    • Measurable decision capability  
    """)

    st.markdown('</div>', unsafe_allow_html=True)

# =====================================================
# KNOWLEDGE STUDIO — DYNAMIC MULTI-PAGE
# =====================================================
with tab2:

    page = st.radio("Select Learning Module:",
        ["1. Foundations",
         "2. Entity Deep Dive",
         "3. Tax Architecture",
         "4. Decision Flow Framework"]
    )

    # PAGE 1
    if page == "1. Foundations":
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Understanding US Legal Structure")

        st.write("""
        The US recognizes both incorporated and unincorporated entities.
        Incorporated → Separate legal personality  
        Unincorporated → Personal exposure risk  
        """)

        time.sleep(0.4)
        st.success("Key Insight: Liability Shield determines structural choice.")

        st.markdown('</div>', unsafe_allow_html=True)

    # PAGE 2
    if page == "2. Entity Deep Dive":
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Graphical Representation of Entities")

        dot = graphviz.Digraph()

        dot.node("US", "US Legal System")
        dot.node("Corp", "Corporations")
        dot.node("Uninc", "Unincorporated Entities")
        dot.node("C", "C-Corp")
        dot.node("S", "S-Corp")
        dot.node("LLC", "LLC")
        dot.node("P", "Partnership")

        dot.edges([
            ("US", "Corp"),
            ("US", "Uninc"),
            ("Corp", "C"),
            ("Corp", "S"),
            ("Uninc", "LLC"),
            ("Uninc", "P")
        ])

        st.graphviz_chart(dot)

        st.info("Notice structural bifurcation between incorporated and flexible entities.")

        st.markdown('</div>', unsafe_allow_html=True)

    # PAGE 3
    if page == "3. Tax Architecture":
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Comparative Tax Matrix")

        df = pd.DataFrame({
            "Entity": ["C-Corp", "S-Corp", "LLC", "Partnership"],
            "Corporate Tax": ["Yes", "No", "Optional", "No"],
            "Dividend Tax": ["Yes", "No", "No", "No"],
            "Pass-through": ["No", "Yes", "Yes", "Yes"]
        })

        st.dataframe(df)

        st.warning("C-Corp → Double taxation risk.")

        st.markdown('</div>', unsafe_allow_html=True)

    # PAGE 4
    if page == "4. Decision Flow Framework":
        st.markdown('<div class="card">', unsafe_allow_html=True)
        st.subheader("Entity Selection Flow")

        dot = graphviz.Digraph()
        dot.node("Start", "Start")
        dot.node("VC", "Seeking Venture Capital?")
        dot.node("CC", "Choose C-Corp")
        dot.node("Flex", "Need Operational Flexibility?")
        dot.node("LL", "Choose LLC")

        dot.edges([
            ("Start", "VC"),
            ("VC", "CC"),
            ("VC", "Flex"),
            ("Flex", "LL")
        ])

        st.graphviz_chart(dot)

        st.markdown('</div>', unsafe_allow_html=True)

# =====================================================
# ADVISORY LAB — REAL LIFE PROBLEM
# =====================================================
with tab3:

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.subheader("Mark & Bill – Advisory Brief")

    st.write("""
    Mark and Bill are California residents.  
    They have been operating informally for 2 years.  
    No written agreement.  
    Thin margins due to boutique intermediaries.  
    100 designs ready for direct sales.  
    They want formal structure and liability protection.
    """)

    st.markdown("### Problems to Analyse")

    st.write("""
    1. Current legal status of their arrangement?  
    2. Personal liability exposure?  
    3. Best suited structure for scalability?  
    4. Impact of taxation under each option?  
    5. Future capital raising considerations?  
    """)

    opinion = st.text_area("Draft structured legal opinion:", height=250)

    if st.button("Preliminary Evaluation"):
        score = 0
        keywords = ["liability", "tax", "partnership", "corporation", "llc"]
        for k in keywords:
            if k in opinion.lower():
                score += 2
        st.success(f"Analytical Depth Score: {score}/10")

    st.markdown('</div>', unsafe_allow_html=True)

# =====================================================
# SIMULATION ARENA — SCENARIO FIRST
# =====================================================
with tab4:

    scenario = st.selectbox("Select Scenario", [
        "Rishee Tech Startup",
        "LawSikho US Expansion",
        "Single Professional Setup",
        "Priyanka Gadget Expansion",
        "Tara Pet Store"
    ])

    st.markdown('<div class="card">', unsafe_allow_html=True)

    # SCENARIO TEXT
    if scenario == "Rishee Tech Startup":
        st.write("High-tech surveillance innovation. Capital intensive. US expansion. Seeking funding.")
    if scenario == "LawSikho US Expansion":
        st.write("Indian ed-tech entering US. Institutional structure required.")
    if scenario == "Single Professional Setup":
        st.write("Individual professional limiting liability.")
    if scenario == "Priyanka Gadget Expansion":
        st.write("Growing product company. Future listing ambition.")
    if scenario == "Tara Pet Store":
        st.write("Single owner, small retail, self-funded.")

    st.markdown("### Now Recommend Suitable Entity")

    entity = st.selectbox("Choose Entity",
        ["C-Corp", "S-Corp", "LLC", "Sole Proprietorship"]
    )

    if st.button("Submit Advisory Decision"):
        st.success("Decision Recorded for Faculty Evaluation")

    st.markdown('</div>', unsafe_allow_html=True)
