import streamlit as st

st.set_page_config(page_title="Corporate Advisory Intelligence", layout="wide")

# -----------------------------
# CORPORATE GLOBAL STYLING
# -----------------------------
st.markdown("""
<style>

/* Remove Streamlit default padding */
.block-container {
    padding-top: 2rem;
    padding-bottom: 2rem;
    padding-left: 3rem;
    padding-right: 3rem;
}

/* Background */
body {
    background-color: #f4f6f9;
}

/* Header */
.main-title {
    font-size: 38px;
    font-weight: 600;
    color: #111827;
    letter-spacing: -0.5px;
}

.subtitle {
    font-size: 16px;
    color: #6b7280;
    margin-top: -8px;
}

/* Card */
.card {
    background: white;
    padding: 35px;
    border-radius: 12px;
    box-shadow: 0 10px 30px rgba(0,0,0,0.05);
    margin-bottom: 30px;
}

/* Section Title */
.section-title {
    font-size: 22px;
    font-weight: 600;
    margin-bottom: 20px;
    color: #1f2937;
}

/* Metric */
.metric-card {
    background: #111827;
    color: white;
    padding: 25px;
    border-radius: 10px;
    text-align: center;
}

/* Buttons */
div.stButton > button {
    background-color: #111827;
    color: white;
    border-radius: 8px;
    padding: 0.6em 1.5em;
    font-weight: 500;
    border: none;
}

div.stButton > button:hover {
    background-color: #1f2937;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------
st.markdown('<div class="main-title">Corporate Advisory Intelligence Platform</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Simulation-Based US Entity & Incorporation Training</div>', unsafe_allow_html=True)
st.markdown("---")

# -----------------------------
# SESSION STATE
# -----------------------------
if "stage" not in st.session_state:
    st.session_state.stage = 1

# -----------------------------
# NAVIGATION
# -----------------------------
col_nav1, col_nav2, col_nav3 = st.columns(3)

with col_nav1:
    if st.button("1️⃣ Learning Module"):
        st.session_state.stage = 1

with col_nav2:
    if st.button("2️⃣ Advisory Scenario"):
        st.session_state.stage = 2

with col_nav3:
    if st.button("3️⃣ Simulation Engine"):
        st.session_state.stage = 3

st.markdown("---")

# -----------------------------
# STAGE 1 — LEARNING
# -----------------------------
if st.session_state.stage == 1:

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">US Business Entity Structures</div>', unsafe_allow_html=True)

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("### C-Corporation")
        st.write("• Separate legal entity")
        st.write("• Double taxation")
        st.write("• Venture capital aligned")
        st.write("• Preferred stock permitted")

        st.markdown("### LLC")
        st.write("• Hybrid structure")
        st.write("• Limited liability")
        st.write("• Flexible taxation")

    with col2:
        st.markdown("### S-Corporation")
        st.write("• Pass-through taxation")
        st.write("• US ownership restriction")
        st.write("• 100 shareholder limit")

        st.markdown("### Partnership")
        st.write("• Flow-through taxation")
        st.write("• Joint liability exposure")

    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# STAGE 2 — ADVISORY SCENARIO
# -----------------------------
if st.session_state.stage == 2:

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Client Advisory Brief</div>', unsafe_allow_html=True)

    st.write("""
Two Indian founders are entering the US market.

• Foreign ownership  
• Multi-member structure  
• Planned $1.2M capital raise  
• Institutional investment expected  

Select the appropriate entity structure.
    """)

    entity = st.selectbox("Recommended Entity",
                          ["C-Corporation", "S-Corporation", "LLC", "Partnership"])

    if st.button("Submit Recommendation"):
        if entity == "C-Corporation":
            st.success("Correct recommendation aligned with venture funding objectives.")
        else:
            st.error("Reconsider investor and ownership implications.")

    st.markdown('</div>', unsafe_allow_html=True)

# -----------------------------
# STAGE 3 — SIMULATION
# -----------------------------
if st.session_state.stage == 3:

    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Delaware Formation Simulation</div>', unsafe_allow_html=True)

    workflow = [
        "Name Reservation",
        "Registered Agent Appointment",
        "Certificate of Formation Drafting",
        "State Filing",
        "Operating Agreement Drafting",
        "EIN Application",
        "BOI Filing (FinCEN)",
        "Corporate Bank Setup"
    ]

    col1, col2 = st.columns([2,1])

    with col1:
        for step in workflow:
            st.write("⬜", step)

    with col2:
        st.markdown('<div class="metric-card">', unsafe_allow_html=True)
        st.write("Compliance Score")
        st.write("100 / 100")
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('</div>', unsafe_allow_html=True)
