import streamlit as st
from database.fetch_data import fetch_students

st.title("Student Performance Analytics Dashboard")

df = fetch_students()

st.subheader("Student Records")
st.dataframe(df)

st.subheader("Basic Statistics")
st.write(df.describe())