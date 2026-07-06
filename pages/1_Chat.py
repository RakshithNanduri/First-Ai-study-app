import streamlit as st
import ollama as ol
import pandas as pd
import os
from pypdf import PdfReader

def ask_ollama(messages):
    response = ol.chat(model="qwen3.5:4b",messages=messages)
    answer = response["message"]["content"]
    return answer

if "chat_id" not in st.session_state:
    st.session_state.chat_id = 1

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hey! How can I help you?"}]

if "show_chat_history" not in st.session_state:
    st.session_state.show_chat_history = False

with st.sidebar:
    st.header('chat options')
    st.header("file context")
    selected_files = []
    if os.path.exists("uploaded_files"):
        saved_files = os.listdir("uploaded_files")
        for saved_file in saved_files:
            if st.checkbox(saved_file):
                selected_files.append(saved_file)
    if st.button("New Chat"):
        st.session_state.messages = [{"role": "assistant", "content": "Hey! How can I help you?"}]
        st.session_state.show_chat_history = False
        st.rerun()
    if st.button("Save Chat"):
        try:
            old_chats = pd.read_csv("Database.csv")
            st.session_state.chat_id = old_chats["chat_id"].max() + 1
        except:
            st.session_state.chat_id = 1

        conversation_df = pd.DataFrame(st.session_state.messages)
        conversation_df["chat_id"] = st.session_state.chat_id
        conversation_df = conversation_df[[ "chat_id","role","content"]]
        conversation_df.to_csv("Database.csv",mode="a",index=False,header=False)
        st.success("Chat Saved!")
    if st.button('load chat'):
        st.session_state.show_chat_history = True
    if st.session_state.show_chat_history:
        try:
            load_conversation=pd.read_csv('Database.csv')
            chat_ids = load_conversation["chat_id"].unique()
            selected_chat = st.selectbox("chat history",chat_ids)
            if st.button("Load Selected Chat"):
                current_chat = load_conversation[load_conversation["chat_id"] == selected_chat]
                st.session_state.messages = current_chat[["role", "content"]].to_dict("records")
                st.success("Chat loaded!")
                st.rerun()
        except FileNotFoundError:
            st.warning("No saved chat found yet.")

for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]
    st.chat_message(role).write(content)

prompt = st.chat_input("Ask me anything")

if prompt:
    context = ""
    for selected_file in selected_files:
        file_path = os.path.join("uploaded_files",selected_file)
        try:
            if selected_file.endswith(".pdf"):
                pdf_reader = PdfReader(file_path)
                pdf_text = ""
                for page in pdf_reader.pages:
                    pdf_text = pdf_text + page.extract_text()
                context = context + "\n\n" + selected_file + ":\n" + pdf_text
            else:
                with open(file_path,"r",encoding="utf-8") as file:
                    context = context + "\n\n" + selected_file + ":\n" + file.read()
        except:
            st.warning(selected_file + " could not be read")

    if context:
        prompt = context + "\n\n" + prompt

    user_message = {"role": "user","content": prompt}
    st.session_state.messages.append(user_message)
    st.chat_message("user").write(prompt)
    reply = ask_ollama(st.session_state.messages)
    assistant_message = {"role": "assistant","content": reply}
    st.session_state.messages.append(assistant_message)
    st.chat_message("assistant").write(reply)
