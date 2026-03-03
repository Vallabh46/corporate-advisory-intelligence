import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(layout="wide")

# =========================
# GLOBAL STYLE
# =========================
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');

.stApp { background-color: white; }

.block-container { padding: 2rem 3rem; }

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

.lesson-video {
    height: 300px;
    background: linear-gradient(90deg, #b11226, #ff4d4d);
    border-radius: 12px;
    margin-bottom: 30px;
    animation: fadeIn 1s ease;
}

@keyframes fadeIn {
    from {opacity:0; transform: translateY(20px);}
    to {opacity:1; transform: translateY(0);}
}

.locked {
    opacity: 0.4;
}
</style>
""", unsafe_allow_html=True)

# =========================
# SESSION STATE
# =========================
if "progress" not in st.session_state:
    st.session_state.progress = 0
    st.session_state.completed_lessons = []
    st.session_state.current_lesson = "Module 1 - Lesson 1"

# =========================
# COURSE STRUCTURE
# =========================
course = {
    "Module 1: Foundations": [
        "Module 1 - Lesson 1",
        "Module 1 - Lesson 2"
    ],
    "Module 2: Tax Architecture": [
        "Module 2 - Lesson 1",
        "Module 2 - Lesson 2"
    ],
    "Module 3: Capital Structuring": [
        "Module 3 - Lesson 1"
    ]
}

# =========================
# SIDEBAR CURRICULUM
# =========================
with st.sidebar:
    st.header("Course Curriculum")

    for module, lessons in course.items():
        st.subheader(module)

        unlocked = True
        if module == "Module 2: Tax Architecture" and "Module 1 - Lesson 2" not in st.session_state.completed_lessons:
            unlocked = False
        if module == "Module 3: Capital Structuring" and "Module 2 - Lesson 2" not in st.session_state.completed_lessons:
            unlocked = False

        for lesson in lessons:
            if lesson in st.session_state.completed_lessons:
                label = f"✔ {lesson} (15 min)"
            else:
                label = f"{lesson} (15 min)"

            if not unlocked:
                st.markdown(f"<div class='locked'>🔒 {label}</div>", unsafe_allow_html=True)
            else:
                if st.button(label):
                    st.session_state.current_lesson = lesson

# =========================
# MAIN CONTENT AREA
# =========================
st.title("US Corporate Advisory Playbook")

# Progress bar
total_lessons = sum(len(v) for v in course.values())
progress_percent = len(st.session_state.completed_lessons) / total_lessons
st.progress(progress_percent)

st.write(f"Course Progress: {int(progress_percent*100)}%")

# =========================
# LESSON CONTENT
# =========================
st.header(st.session_state.current_lesson)

# Video-like animated section
st.markdown("<div class='lesson-video'></div>", unsafe_allow_html=True)

if st.session_state.current_lesson == "Module 1 - Lesson 1":
    st.write("""
When entering the United States market, the first legal decision an entrepreneur must take is the choice of entity. 
This decision determines liability allocation, taxation structure, and governance architecture.
    """)

elif st.session_state.current_lesson == "Module 1 - Lesson 2":
    st.write("""
A corporation exists as a separate legal personality. 
It shields shareholders through the corporate veil, 
provided formalities are respected.
    """)

elif st.session_state.current_lesson == "Module 2 - Lesson 1":
    st.write("""
Taxation architecture is central to structural design. 
C-Corporations face double taxation, whereas LLCs may elect pass-through treatment.
    """)

elif st.session_state.current_lesson == "Module 2 - Lesson 2":
    st.write("""
S-Corporations provide pass-through taxation but impose ownership restrictions.
They cannot have foreign shareholders.
    """)

elif st.session_state.current_lesson == "Module 3 - Lesson 1":
    st.write("""
Capital structuring is decisive when venture funding is anticipated.
Only C-Corporations permit multiple classes of stock.
    """)

# =========================
# COMPLETE LESSON BUTTON
# =========================
if st.button("Mark Lesson Complete"):
    if st.session_state.current_lesson not in st.session_state.completed_lessons:
        st.session_state.completed_lessons.append(st.session_state.current_lesson)

# =========================
# CONTINUE LEARNING
# =========================
def next_lesson():
    lessons_flat = [l for lessons in course.values() for l in lessons]
    current_index = lessons_flat.index(st.session_state.current_lesson)
    if current_index + 1 < len(lessons_flat):
        return lessons_flat[current_index + 1]
    return None

next_l = next_lesson()
if next_l:
    if st.button("Continue Learning"):
        st.session_state.current_lesson = next_l
