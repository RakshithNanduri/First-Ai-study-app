import streamlit as st
import os


st.title("Resources")
st.caption("Upload notes or PDFs here, then select them from the Chat page sidebar.")

if not os.path.exists("uploaded_files"):
    os.makedirs("uploaded_files")

uploaded_files = st.file_uploader("Upload study files", accept_multiple_files=True)

if uploaded_files:
    for uploaded_file in uploaded_files:
        file_path = os.path.join("uploaded_files", uploaded_file.name)

        with open(file_path, "wb") as file:
            file.write(uploaded_file.getbuffer())

        st.success(uploaded_file.name + " saved")

st.header("Saved Files")

saved_files = os.listdir("uploaded_files")

for saved_file in saved_files:
    file_path = os.path.join("uploaded_files", saved_file)

    st.write(saved_file)

    if st.button("Delete", key="delete_" + saved_file):
        os.remove(file_path)
        st.success(saved_file + " deleted")
        st.rerun()
