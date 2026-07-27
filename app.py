import streamlit as st

# ---------------- Page Config ----------------
st.set_page_config(
    page_title="AI Student Performance Predictor",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------- Custom CSS ----------------
st.markdown("""
<style>

.main{
    background-color:#F5F7FA;
}

.hero{
    background:linear-gradient(90deg,#2563EB,#7C3AED);
    padding:35px;
    border-radius:18px;
    color:white;
    text-align:center;
    margin-bottom:30px;
}

div[data-testid="metric-container"]{
    background:white;
    padding:18px;
    border-radius:12px;
    box-shadow:0px 3px 10px rgba(0,0,0,0.15);
}

</style>
""", unsafe_allow_html=True)

# ---------------- Hero ----------------
st.markdown("""
<div class="hero">

<h1>🎓 AI-Powered Student Performance Predictor</h1>

<h4>Predict • Analyze • Improve Student Success</h4>

</div>
""", unsafe_allow_html=True)

# ---------------- Metrics ----------------
col1,col2,col3,col4 = st.columns(4)

with col1:
    st.metric("Students", "5000")

with col2:
    st.metric("Model", "Random Forest")

with col3:
    st.metric("Accuracy", "85.7%")

with col4:
    st.metric("Features", "19")

st.divider()

st.header("📌 Project Overview")

st.write("""
This application predicts a student's academic performance using a
Machine Learning model trained on student academic and behavioral data.

### Features

- 🎯 Student Performance Prediction
- 📊 Interactive Dashboard
- 📈 Data Analytics
- 📂 Dataset Explorer
- 🤖 Machine Learning Prediction
- 📑 Model Evaluation
""")

st.success("👈 Use the sidebar to navigate through different pages.")