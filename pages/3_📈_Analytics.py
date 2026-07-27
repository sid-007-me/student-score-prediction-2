import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Analytics", layout="wide")

st.title("📈 Student Performance Analytics")

# Load dataset
df = pd.read_csv("data/student_performance_realistic_5000.csv")

# Sidebar Filter
st.sidebar.header("Filters")

grade = st.sidebar.multiselect(
    "Grade Level",
    df["Grade_Level"].unique(),
    default=df["Grade_Level"].unique()
)

filtered_df = df[df["Grade_Level"].isin(grade)]

# Row 1
col1, col2 = st.columns(2)

with col1:
    fig = px.scatter(
        filtered_df,
        x="Attendance",
        y="Previous_GPA",
        color="Performance",
        title="Attendance vs GPA"
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    fig = px.box(
        filtered_df,
        x="Performance",
        y="Study_Hours_Per_Day",
        color="Performance",
        title="Study Hours by Performance"
    )
    st.plotly_chart(fig, use_container_width=True)

# Row 2
col3, col4 = st.columns(2)

with col3:
    fig = px.histogram(
        filtered_df,
        x="Stress_Level",
        color="Performance",
        barmode="group",
        title="Stress Level Distribution"
    )
    st.plotly_chart(fig, use_container_width=True)

with col4:
    fig = px.bar(
        filtered_df.groupby("Performance")["Attendance"].mean().reset_index(),
        x="Performance",
        y="Attendance",
        color="Performance",
        title="Average Attendance by Performance"
    )
    st.plotly_chart(fig, use_container_width=True)

st.divider()

st.subheader("Correlation Heatmap")

corr = filtered_df.select_dtypes(include="number").corr()

fig = px.imshow(
    corr,
    text_auto=True,
    aspect="auto",
    color_continuous_scale="Viridis"
)

st.plotly_chart(fig, use_container_width=True)