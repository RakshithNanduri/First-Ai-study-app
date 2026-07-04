import streamlit as st
import ollama as ol
import pandas as pd
prompt=''

def ask_streamlit(prompt):
    response=ol.chat(model=('qwen3:latest'), messages=[{'role': 'user', 'content': prompt}])
    return response['message']['content']

if 'messages' not in st.session_state:
    st.chat_message('assistant').write('Hi! how can i assist you today??')

prompt = st.chat_input("Ask me anything", key="input")

if prompt:
    st.chat_message("user").write(prompt)
    reply=ask_streamlit(prompt)
    st.spinner("Wait for it...", show_time=True)
    st.chat_message('assistant').write(reply)
