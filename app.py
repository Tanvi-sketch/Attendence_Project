import streamlit as st
from utils import attendance_percentage, max_bunks, classes_needed
from model import predict_status

# ---------- PAGE CONFIG ----------
st.set_page_config(page_title="Smart Attendance", page_icon="🎓", layout="wide")

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>
body { background-color: #f5f7fa; }
.title { text-align:center; color:#2c3e50; font-size:42px; font-weight:700; }
.card { padding:20px; border-radius:16px; background:#ffffff;
        box-shadow:0 6px 18px rgba(0,0,0,0.08); margin-bottom:15px; }
.small { color:#7f8c8d; }
.footer { text-align:center; color:#95a5a6; margin-top:30px; }
</style>
""", unsafe_allow_html=True)

# ---------- SIMPLE LOGIN ----------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

def login():
    st.markdown('<div class="title">🔐 Login</div>', unsafe_allow_html=True)
    with st.container():
        st.markdown('<div class="card">', unsafe_allow_html=True)
        user = st.text_input("Username")
        pwd = st.text_input("Password", type="password")

        if st.button("Login"):
            if user == "MIT" and pwd == "7890":
                st.session_state.logged_in = True
                st.success("Login successful")
            else:
                st.error("Invalid credentials")
        st.markdown('</div>', unsafe_allow_html=True)

if not st.session_state.logged_in:
    login()
    st.stop()

# ---------- SIDEBAR ----------
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to", ["Dashboard", "Analyzer", "About"])

# ---------- HEADER ----------
st.markdown('<div class="title">🎓 Smart Attendance Analyzer</div>', unsafe_allow_html=True)
st.markdown('<p class="small" style="text-align:center;">Track, predict, and plan your attendance smartly</p>', unsafe_allow_html=True)

# ---------- DASHBOARD ----------
if page == "Dashboard":
    st.markdown("### 📊 Overview")

    col1, col2, col3 = st.columns(3)
    col1.metric("Target %", "75%")
    col2.metric("Model", "Logistic Regression")
    col3.metric("Range", "10–80 classes")

    st.markdown("### 📈 Sample Trend")
    st.line_chart([60, 65, 70, 72, 75, 78])

# ---------- ANALYZER ----------
elif page == "Analyzer":
    st.markdown("### 🔍 Attendance Analyzer")

    st.markdown('<div class="card">', unsafe_allow_html=True)

    col1, col2 = st.columns(2)
    with col1:
        total = st.number_input("Total Classes", min_value=1)
    with col2:
        attended = st.number_input("Classes Attended", min_value=0)

    analyze = st.button("Analyze")

    st.markdown('</div>', unsafe_allow_html=True)

    if analyze:
        if attended > total:
            st.error("Attended cannot be greater than total")
        else:
            percent = attendance_percentage(total, attended)
            status = predict_status(total, attended)

            st.markdown("### 📊 Results")
            c1, c2 = st.columns(2)
            c1.metric("Attendance %", f"{percent:.2f}%")
            c2.metric("Status", status)

            if percent >= 75:
                st.success(f"✅ Safe! You can bunk {max_bunks(total, attended)} classes")
            else:
                st.error(f"⚠️ Risk! Attend next {classes_needed(total, attended)} classes")

            st.markdown("### 📉 Visual")
            st.progress(min(int(percent), 100))

# ---------- ABOUT ----------
elif page == "About":
    st.markdown("### ℹ️ About Project")
    st.write("""
    This project helps students:
    - Track attendance percentage  
    - Predict Safe/Risk using ML  
    - Plan classes smartly  

    **Tech Used:**
    - Python  
    - scikit-learn  
    - Streamlit  
    """)
