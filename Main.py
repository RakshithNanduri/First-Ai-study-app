import streamlit as st


st.set_page_config(page_title="AI Study Companion")

st.title("AI Study Companion")
st.write(
    "A beginner-friendly study app that uses local Ollama models to answer "
    "questions, explain notes, and help with revision."
)

st.divider()

st.subheader("Current Features")
st.markdown(
    """
- Chat with a local AI model
- Study tutor style answers
- Save and load chat history
- Upload notes and PDFs for context
- Choose between a general model and a coding model
"""
)

st.subheader("How to Use")
st.markdown(
    """
1. Open the **Chat** page from the sidebar.
2. Ask a study question.
3. Upload notes from the **Resources** page if needed.
4. Select uploaded files in the Chat sidebar.
5. Ask questions about your notes.
"""
)

st.subheader("Learning Goal")
st.write(
    "This project is built to practice Python, Streamlit, local AI with Ollama, "
    "file handling, and GitHub workflow."
)
