import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Dashboard", layout="wide")

# ---------------- Load Data ----------------

df = pd.read_csv("data/student_performance_realistic_5000.csv")

# ---------------- Title ----------------

st.title("📊 Student Dashboard")
st.write("Explore student statistics and academic insights.")

# ---------------- Sidebar Filters ----------------

st.sidebar.header("🔍 Filters")

gender = st.sidebar.multiselect(
    "Select Gender",
    options=df["Gender"].unique(),
    default=df["Gender"].unique()
)

grade = st.sidebar.multiselect(
    "Select Grade",
    options=df["Grade_Level"].unique(),
    default=df["Grade_Level"].unique()
)

filtered_df = df[
    (df["Gender"].isin(gender)) &
    (df["Grade_Level"].isin(grade))
]

# ---------------- KPI Cards ----------------

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric("👨‍🎓 Students", len(filtered_df))

with col2:
    st.metric(
        "📅 Avg Attendance",
        f"{filtered_df['Attendance'].mean():.1f}%"
    )

with col3:
    st.metric(
        "📚 Avg Study Hours",
        round(filtered_df["Study_Hours_Per_Day"].mean(),2)
    )

with col4:
    st.metric(
        "🎯 Avg GPA",
        round(filtered_df["Previous_GPA"].mean(),2)
    )

st.divider()

# ---------------- Charts ----------------

col1, col2 = st.columns(2)

with col1:

    fig = px.histogram(
        filtered_df,
        x="Attendance",
        nbins=20,
        color_discrete_sequence=["royalblue"],
        title="Attendance Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

with col2:

    fig = px.histogram(
        filtered_df,
        x="Study_Hours_Per_Day",
        nbins=20,
        color_discrete_sequence=["green"],
        title="Study Hours Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

# ---------------- Second Row ----------------

col3, col4 = st.columns(2)

with col3:

    fig = px.pie(
        filtered_df,
        names="Performance",
        title="Performance Distribution"
    )

    st.plotly_chart(fig, use_container_width=True)

with col4:

    fig = px.bar(
        filtered_df["Grade_Level"].value_counts().reset_index(),
        x="Grade_Level",
        y="count",
        color="Grade_Level",
        title="Students by Grade"
    )

    st.plotly_chart(fig, use_container_width=True)