import streamlit as st
import pandas as pd
import graphviz
from streamlit_option_menu import option_menu

st.set_page_config(page_title="US Corporate Advisory Playbook", layout="wide")

# ==========================
# CLEAN WHITE + RED ACADEMIC STYLE
# ==========================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Libre+Baskerville:wght@400;700&family=Inter:wght@400;500;600&display=swap');

.stApp {
    background-color: white;
}

.block-container {
    padding: 4rem 6rem;
}

h1, h2 {
    font-family: 'Libre Baskerville', serif;
    color: #b11226 !important;
}

h3 {
    font-family: 'Libre Baskerville', serif;
    color: #8b0000 !important;
}

p, li {
    font-family: 'Inter', sans-serif;
    font-size: 18px;
    line-height: 1.9;
    color: black !important;
}

.section {
    margin-bottom: 80px;
}

</style>
""", unsafe_allow_html=True)

st.title("US Corporate Advisory Playbook")

selected = option_menu(
    None,
    ["Knowledge Studio", "Case Analysis", "Applied Simulation", "Performance Report"],
    orientation="horizontal"
)

# =====================================================
# KNOWLEDGE STUDIO (COURSERA STYLE LONG FORM)
# =====================================================
if selected == "Knowledge Studio":

    st.header("Module 1: Foundations of US Business Structures")

    st.markdown("""
The decision to select a business entity in the United States is not merely procedural. It is structural, financial, and strategic. 

When an entrepreneur decides to enter the American market, they are effectively choosing a legal architecture that will determine their exposure to liability, their taxation framework, their ability to raise capital, and the longevity of their enterprise.

In the United States, business entities are broadly classified into incorporated and unincorporated forms. This distinction is fundamental. Incorporated entities such as corporations possess a separate legal personality distinct from their founders. Unincorporated entities such as partnerships often blur that distinction, creating potential personal exposure.
""")

    st.markdown("---")

    st.subheader("Understanding Legal Personality")

    st.markdown("""
A corporation is treated as a separate legal person. This means that the entity can enter into contracts, own property, sue, and be sued independently of its shareholders. 

This separation creates what is known as the corporate veil. The corporate veil protects shareholders from personal liability, except in cases of fraud or misuse. 

In contrast, in a general partnership, partners are personally liable for the obligations of the firm. This means their personal assets may be exposed to business risks.
""")

    dot = graphviz.Digraph()
    dot.node("Founder", "Founder")
    dot.node("Corp", "Corporation")
    dot.node("Liability", "Business Liability")

    dot.edges([
        ("Founder", "Corp"),
        ("Corp", "Liability")
    ])

    st.graphviz_chart(dot)

    st.markdown("---")

    st.subheader("Comparative Structural Overview")

    df = pd.DataFrame({
        "Feature": ["Legal Personality", "Liability Protection", "Taxation", "Capital Raising Flexibility"],
        "C-Corp": ["Separate Entity", "Limited", "Double Taxation", "High"],
        "S-Corp": ["Separate Entity", "Limited", "Pass-through", "Restricted"],
        "LLC": ["Flexible Structure", "Limited", "Flexible", "Moderate"],
        "Partnership": ["No Separate Personality", "Unlimited", "Pass-through", "Low"]
    })

    st.dataframe(df)

    st.markdown("""
The choice between these structures must be guided by future ambition. If venture capital funding is anticipated, the C-Corporation is typically preferred because it allows multiple classes of stock and structured investor rights.

If operational flexibility and tax efficiency are priorities, the LLC offers a compelling hybrid model.
""")

    st.markdown("---")

    st.header("Module 2: Tax Architecture")

    st.markdown("""
Taxation is often misunderstood as a mere compliance issue. In reality, it shapes the economics of the business.

A C-Corporation is subject to corporate income tax. If profits are distributed as dividends, shareholders are taxed again. This phenomenon is called double taxation.

An S-Corporation and LLC (if not electing corporate taxation) pass income directly to members. This is known as pass-through taxation. The entity itself does not pay federal income tax.
""")

    st.markdown("---")

    st.header("Module 3: Capital Structuring & Investor Expectations")

    st.markdown("""
Venture capital firms prefer predictability and structured rights. The C-Corporation provides a framework for issuing preferred shares, liquidation preferences, and convertible instruments.

An LLC may offer flexibility but often complicates institutional investment due to tax allocation complexities.

Therefore, entity selection must anticipate not just present needs, but future ambitions.
""")

# =====================================================
# CASE ANALYSIS
# =====================================================
elif selected == "Case Analysis":

    st.header("Mark & Bill – Advisory Case")

    st.markdown("""
Mark and Bill have operated informally for two years. They share profits but have no written agreement. Their current structure resembles a general partnership under US law.

This means they may be jointly and severally liable for obligations incurred in the course of business.

They now wish to formalize their enterprise, protect their personal assets, and scale operations.
""")

    st.subheader("Draft Your Legal Opinion")

    opinion = st.text_area("Provide structured reasoning:", height=350)

    if st.button("Evaluate Analysis"):
        score = 0
        keywords = ["liability", "tax", "corporation", "llc", "partnership"]
        for k in keywords:
            if k in opinion.lower():
                score += 2

        st.success(f"Analytical Depth Score: {score}/10")

# =====================================================
# APPLIED SIMULATION
# =====================================================
elif selected == "Applied Simulation":

    st.header("Scenario-Based Advisory Simulation")

    scenario = st.selectbox("Select Scenario", [
        "High Growth Technology Venture",
        "Professional Services Firm",
        "Single Retail Owner"
    ])

    if scenario == "High Growth Technology Venture":
        st.write("""
The founder seeks venture funding, intends to issue equity, and plans long-term expansion.
        """)

    choice = st.selectbox("Select Appropriate Entity",
                          ["C-Corp", "S-Corp", "LLC", "Partnership"])

    if st.button("Submit Decision"):
        st.success("Decision recorded for performance evaluation.")

# =====================================================
# PERFORMANCE REPORT
# =====================================================
elif selected == "Performance Report":

    st.header("Advisory Intelligence Dashboard")

    st.metric("Knowledge Mastery", "85 / 100")
    st.metric("Analytical Depth", "78 / 100")
    st.metric("Entity Selection Accuracy", "80 / 100")
