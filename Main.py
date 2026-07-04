import streamlit as st
st.set_page_config(page_title="My Ai study App", page_icon="😊", layout="wide")
col1, col2 = st.columns(2)
with col1:
    st.title("My Ai study App")
    st.write("Welcome to the app!")
with col2:
    st.image('image.png', width=100, caption="My Ai study App", output_format="auto")
    
