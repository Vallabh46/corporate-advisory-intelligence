import streamlit as st
import pandas as pd
import graphviz
from streamlit_option_menu import option_menu

st.set_page_config(page_title="Corporate Advisory Playbook", layout="wide")

# ===============================
# PREMIUM WHITE + RED STYLING
# ===============================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@500;700&family=Inter:wght@400;600&display=swap');

.stApp {
    background-color: white;
}

.block-container {
    padding: 3rem 4rem;
}

h1, h2, h3 {
    color: #a50000 !important;
    font-family: 'Playfair Display', serif;
}

p, label {
    color: black !important;
    font-family: 'Inter', sans-serif;
    font-size: 17px;
    line-height: 1.7;
}

.section {
    margin-bottom: 50px;
}

.card {
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0 6px 25px rgba(0,0,0,0.08);
    margin-bottom: 40px;
}

</style>
""", unsafe_allow_html=True)

st.title("US Corporate Advisory Playbook")

# ===============================
# NAVIGATION MENU
# ===============================
selected = option_menu(
    menu_title=None,
    options=["Knowledge Studio", "Advisory Playbook", "Simulation Arena", "Performance Dashboard"],
    orientation="horizontal"
)

# =====================================================
# KNOWLEDGE STUDIO
# =====================================================
if selected == "Knowledge Studio":

    st.header("Understanding the Architecture of US Business Entities")

    st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/5/5a/Business_structure_chart.svg/800px-Business_structure_chart.svg.png")

    st.markdown("""
When we speak of business entities in the United States, we are not merely referring to labels such as “LLC” or “Corporation.” We are speaking about structures that determine how power flows, how profits are distributed, how taxes are calculated, and most importantly, how liability is allocated.

Imagine two founders standing at the beginning of a journey. Their first legal decision will shape their exposure to risk, their fundraising potential, their operational flexibility, and their long-term exit strategy. The choice of entity is not administrative — it is architectural.

A C-Corporation is traditionally structured as a separate legal personality. It stands apart from its founders. It can sue and be sued. It pays its own taxes. It is the preferred vehicle for venture capital because it permits multiple classes of stock and structured investment instruments.

An LLC, on the other hand, blends the flexibility of partnerships with the liability shield of corporations. It allows members to define their internal economic arrangements contractually. It offers remarkable flexibility in taxation elections.

An S-Corporation provides pass-through taxation but imposes structural limitations that restrict ownership flexibility.

A partnership, while easy to form, exposes partners to personal liability unless carefully structured.
    """)

    st.video("https://www.youtube.com/watch?v=Qp6i1n1J3_E")  # placeholder video

    st.markdown("""
The true sophistication of advisory lies in understanding when structural rigidity benefits growth and when flexibility preserves survival. This distinction separates transactional drafting from strategic advisory.
    """)

# =====================================================
# ADVISORY PLAYBOOK
# =====================================================
elif selected == "Advisory Playbook":

    st.header("Mark & Bill – Strategic Advisory Case")

    st.markdown("""
Mark and Bill are not merely designers. They are entrepreneurs standing at a structural crossroads.

For two years, their business relationship has functioned informally. There are no written agreements. Profits are divided by mutual understanding. Their liability is unstructured. If a customer files a lawsuit tomorrow, who bears the burden? If a supplier sues for non-payment, whose personal assets are at risk?

Now they wish to formalize their enterprise.

The legal question is not only: “What entity should they choose?”

The deeper question is: “What risk profile are they willing to accept?”
    """)

    st.subheader("Draft Your Legal Opinion")

    opinion = st.text_area("Provide structured advisory reasoning:", height=300)

    if st.button("Evaluate Opinion"):
        score = 0
        keywords = ["liability", "taxation", "limited", "corporation", "llc", "partnership"]
        for word in keywords:
            if word in opinion.lower():
                score += 2

        st.success(f"Analytical Advisory Score: {score}/12")

# =====================================================
# SIMULATION ARENA
# =====================================================
elif selected == "Simulation Arena":

    st.header("Entity Selection Simulation")

    scenario = st.selectbox("Select Scenario", [
        "Rishee – Tech Expansion",
        "LawSikho – US Branch",
        "Priyanka – Scaling Innovation",
        "Tara – Sole Retail Setup"
    ])

    if scenario == "Rishee – Tech Expansion":
        st.markdown("""
Rishee has developed a technological surveillance solution that requires capital-intensive infrastructure. He seeks entry into the United States market, anticipating investor funding and scalable growth. The entity must allow structured capital infusion and potential listing in the future.
        """)

    entity = st.selectbox("Select Appropriate Entity",
                          ["C-Corp", "LLC", "S-Corp", "Sole Proprietorship"])

    if st.button("Submit Advisory Decision"):
        st.success("Advisory decision recorded.")

# =====================================================
# PERFORMANCE DASHBOARD
# =====================================================
elif selected == "Performance Dashboard":

    st.header("Advisory Performance Metrics")

    st.metric("Advisory Depth Index", "82 / 100")
    st.metric("Tax Reasoning Score", "75 / 100")
    st.metric("Liability Risk Sensitivity", "88 / 100")
    st.metric("Entity Selection Accuracy", "80 / 100")
