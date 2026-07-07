import streamlit as st
import os


st.title("Resources")

if not os.path.exists("uploaded_files"):
    os.makedirs("uploaded_files")

uploaded_files = st.file_uploader("Upload files", accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        file_path = os.path.join("uploaded_files", uploaded_file.name)

        with open(file_path, "wb") as file:
            file.write(uploaded_file.getbuffer())

        st.success(uploaded_file.name + " saved")

st.header("Saved files")

saved_files = os.listdir("uploaded_files")

for saved_file in saved_files:
    st.write(saved_file)
