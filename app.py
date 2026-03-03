import streamlit as st

st.set_page_config(
    page_title="Corporate Advisory Intelligence",
    layout="wide",
)

# ------------------------------
# CORPORATE THEME
# ------------------------------
st.markdown("""
<style>
body {
    background-color: #f5f7fa;
}
.main-title {
    font-size: 34px;
    font-weight: 600;
    color: #1a1f36;
}
.subtitle {
    font-size: 16px;
    color: #5a6270;
}
.card {
    background: white;
    padding: 30px;
    border-radius: 10px;
    box-shadow: 0 4px 20px rgba(0,0,0,0.04);
    margin-bottom: 25px;
}
.section-title {
    font-size: 20px;
    font-weight: 600;
    margin-bottom: 15px;
}
</style>
""", unsafe_allow_html=True)

# ------------------------------
# HEADER
# ------------------------------
st.markdown('<div class="main-title">Corporate Advisory Intelligence Platform</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Simulation-Based US Entity & Incorporation Training</div>', unsafe_allow_html=True)
st.markdown("---")

# ------------------------------
# NAVIGATION STATE
# ------------------------------
if "stage" not in st.session_state:
    st.session_state.stage = 1

# ------------------------------
# STAGE 1 — LEARNING MODULE
# ------------------------------
if st.session_state.stage == 1:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Module 1 — US Business Entities</div>', unsafe_allow_html=True)

    st.markdown("""
**C-Corporation**
- Separate legal entity
- Double taxation
- Preferred stock permitted
- Venture capital aligned

**S-Corporation**
- Pass-through taxation
- US ownership restrictions
- 100 shareholder cap

**LLC**
- Flexible hybrid structure
- Limited liability
- Operational simplicity

**Partnership**
- Pass-through taxation
- Joint liability exposure
    """)

    if st.button("Proceed to Advisory Scenario"):
        st.session_state.stage = 2

    st.markdown('</div>', unsafe_allow_html=True)

# ------------------------------
# STAGE 2 — SCENARIO PLACEHOLDER
# ------------------------------
if st.session_state.stage == 2:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Module 2 — Advisory Scenario</div>', unsafe_allow_html=True)

    st.write("Scenario logic will be implemented next.")

    if st.button("Proceed to Simulation"):
        st.session_state.stage = 3

    st.markdown('</div>', unsafe_allow_html=True)

# ------------------------------
# STAGE 3 — SIMULATION PLACEHOLDER
# ------------------------------
if st.session_state.stage == 3:
    st.markdown('<div class="card">', unsafe_allow_html=True)
    st.markdown('<div class="section-title">Module 3 — Procedural Simulation</div>', unsafe_allow_html=True)

    st.write("Simulation engine will be implemented next.")

    st.markdown('</div>', unsafe_allow_html=True)
