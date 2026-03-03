import streamlit as st

st.set_page_config(page_title="US Corporate Advisory Playbook", layout="wide")

# ===============================
# STYLE (MODERN COURSE PLATFORM)
# ===============================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');

.stApp {
    background-color: white;
}

.block-container {
    padding: 0rem 8rem;
}

h1, h2, h3 {
    font-family: 'Poppins', sans-serif;
    color: #b11226 !important;
}

p {
    font-family: 'Poppins', sans-serif;
    font-size: 18px;
    line-height: 1.8;
    color: black !important;
}

.hero {
    padding: 4rem 0rem 3rem 0rem;
    border-bottom: 1px solid #eee;
}

.course-card {
    border: 1px solid #eee;
    border-radius: 10px;
    padding: 25px;
    margin-bottom: 25px;
    transition: 0.3s ease;
}

.course-card:hover {
    box-shadow: 0 6px 20px rgba(0,0,0,0.08);
    transform: translateY(-4px);
}

.section-content {
    padding: 3rem 0rem;
}

</style>
""", unsafe_allow_html=True)

# ===============================
# HERO SECTION
# ===============================
st.markdown("<div class='hero'>", unsafe_allow_html=True)
st.title("US Corporate Advisory Playbook")
st.write("""
Master the structural architecture of US business entities through
deep analysis, applied case studies, and decision-based simulations.

This is not theory. This is structured advisory intelligence.
""")
st.markdown("</div>", unsafe_allow_html=True)

# ===============================
# COURSE CURRICULUM SECTION
# ===============================
st.header("Curriculum")

if "module" not in st.session_state:
    st.session_state.module = None

modules = {
    "Foundations of US Business Structures":
        "Understand legal personality, liability shields, and entity classification.",
    "Taxation Architecture & Economic Impact":
        "Deep dive into corporate taxation, pass-through entities, and structural tax consequences.",
    "Capital Structuring & Venture Expectations":
        "Learn how entity choice affects funding, equity structuring, and exit strategies.",
    "Applied Advisory Case Study":
        "Analyse Mark & Bill’s scenario and develop a structured legal opinion.",
    "Strategic Simulation Lab":
        "Test your advisory intelligence through decision-based entity simulations."
}

for title, desc in modules.items():
    st.markdown("<div class='course-card'>", unsafe_allow_html=True)
    st.subheader(title)
    st.write(desc)

    if st.button(f"Open Module: {title}"):
        st.session_state.module = title

    st.markdown("</div>", unsafe_allow_html=True)

# ===============================
# MODULE VIEW
# ===============================
if st.session_state.module:

    st.markdown("<div class='section-content'>", unsafe_allow_html=True)
    st.header(st.session_state.module)

    if st.session_state.module == "Foundations of US Business Structures":

        st.write("""
When entrepreneurs enter the United States market, their first structural decision
is the selection of a legal entity. This choice determines whether the business
is treated as an independent legal personality or merely an extension of its founders.

A corporation stands separate from its shareholders.
It can sue, be sued, own property, and incur liabilities independently.
This separation forms the foundation of the corporate veil.

In contrast, a partnership exposes partners to personal liability.
If the firm defaults, personal assets may be at risk.
""")

        st.write("""
The distinction between incorporated and unincorporated entities
is not merely academic — it determines the allocation of risk.
""")

    if st.session_state.module == "Taxation Architecture & Economic Impact":

        st.write("""
Taxation in the United States is structurally tied to entity form.

A C-Corporation is subject to corporate income tax.
If dividends are distributed, shareholders are taxed again.
This creates the phenomenon of double taxation.

An LLC may elect pass-through taxation.
This means profits are taxed once at the member level.
""")

    if st.session_state.module == "Applied Advisory Case Study":

        st.write("""
Mark and Bill have operated informally for two years.
Their arrangement resembles a general partnership.
They now seek structural protection and scalability.

Your task is to draft a legal opinion advising them on:
• Liability implications
• Tax considerations
• Future capital ambitions
""")

        opinion = st.text_area("Draft your legal opinion:", height=300)

        if st.button("Submit Opinion"):
            st.success("Opinion submitted for review.")

    if st.session_state.module == "Strategic Simulation Lab":

        st.write("""
You will now enter a decision-based advisory simulation.
Each scenario will test your ability to align entity choice
with liability, taxation, and funding objectives.
""")

    if st.button("Back to Curriculum"):
        st.session_state.module = None

    st.markdown("</div>", unsafe_allow_html=True)
