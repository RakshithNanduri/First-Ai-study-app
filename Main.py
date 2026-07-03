import streamlit as st
st.title("My Ai study App")
question: str= st.text_input("Enter your question here")
st.button("Submit")
st.write(f"You asked: , {question}")

