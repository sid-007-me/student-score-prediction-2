import streamlit as st
import pandas as pd

st.set_page_config(page_title="Dataset", layout="wide")

st.title("📂 Student Dataset Explorer")

# Load Dataset
df = pd.read_csv("data/student_performance_realistic_5000.csv")

st.write(f"### Total Records: {len(df)}")
st.write(f"### Total Columns: {len(df.columns)}")

st.divider()

# Search
search = st.text_input("🔍 Search Student")

if search:
    filtered = df[df.astype(str).apply(
        lambda row: row.str.contains(search, case=False).any(),
        axis=1
    )]
    st.dataframe(filtered, use_container_width=True)
else:
    st.dataframe(df, use_container_width=True)

st.divider()

st.subheader("Dataset Information")

info = pd.DataFrame({
    "Column Name": df.columns,
    "Data Type": df.dtypes.astype(str)
})

st.dataframe(info, use_container_width=True)

st.divider()

csv = df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="⬇ Download Dataset",
    data=csv,
    file_name="student_performance.csv",
    mime="text/csv"
)