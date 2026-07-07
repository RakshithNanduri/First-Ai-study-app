import streamlit as st
import ollama as ol
import pandas as pd
import os
from pypdf import PdfReader


def ask_ollama(messages, model_name):
    try:
        response = ol.chat(model=model_name, messages=messages)
        answer = response["message"]["content"]

        if answer.strip() == "":
            return "Ollama returned an empty answer. Please try again."

        return answer

    except Exception:
        return "Ollama is not running or the model name is wrong. Please check Ollama and try again."


if "chat_id" not in st.session_state:
    st.session_state.chat_id = 1

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hey! How can I help you?"}
    ]

if "show_chat_history" not in st.session_state:
    st.session_state.show_chat_history = False

with st.sidebar:
    st.header("Chat options")
    use_coding_model = st.checkbox("Use coding model")

    if use_coding_model:
        model_name = "qwen 3.5:4b"
    else:
        model_name = "llama3.2"

    st.write("Model:", model_name)

    st.header("File context")

    selected_files = []

    if os.path.exists("uploaded_files"):
        saved_files = os.listdir("uploaded_files")

        for saved_file in saved_files:
            if st.checkbox(saved_file):
                selected_files.append(saved_file)

    if st.button("New Chat"):
        st.session_state.messages = [
            {"role": "assistant", "content": "Hey! How can I help you?"}
        ]
        st.session_state.show_chat_history = False
        st.rerun()

    if st.button("Save Chat"):
        try:
            old_chats = pd.read_csv("Database.csv")
            st.session_state.chat_id = old_chats["chat_id"].max() + 1
        except Exception:
            st.session_state.chat_id = 1

        conversation_df = pd.DataFrame(st.session_state.messages)
        conversation_df["chat_id"] = st.session_state.chat_id
        conversation_df = conversation_df[["chat_id", "role", "content"]]
        conversation_df.to_csv("Database.csv", mode="a", index=False, header=False)
        st.success("Chat Saved!")

    if st.button("Load chat"):
        st.session_state.show_chat_history = True

    if st.session_state.show_chat_history:
        try:
            load_conversation = pd.read_csv("Database.csv")
            chat_ids = load_conversation["chat_id"].unique()
            selected_chat = st.selectbox("Chat history", chat_ids)

            if st.button("Load Selected Chat"):
                current_chat = load_conversation[
                    load_conversation["chat_id"] == selected_chat
                ]
                st.session_state.messages = current_chat[["role", "content"]].to_dict(
                    "records"
                )
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

    if prompt.strip() == "":
        st.warning("Please enter a question first.")
    else:
        original_prompt = prompt

        for selected_file in selected_files:
            file_path = os.path.join("uploaded_files", selected_file)

            try:
                if selected_file.endswith(".pdf"):
                    pdf_reader = PdfReader(file_path)
                    pdf_text = ""

                    for page in pdf_reader.pages:
                        pdf_text = pdf_text + page.extract_text()

                    context = context + "\n\n" + selected_file + ":\n" + pdf_text
                else:
                    with open(file_path, "r", encoding="utf-8") as file:
                        context = context + "\n\n" + selected_file + ":\n" + file.read()
            except Exception:
                st.warning(selected_file + " could not be read")

        study_prompt = (
            "You are a beginner-friendly study tutor. "
            "Explain clearly, give an example if useful, "
            "and keep the answer short.\n\n"
        )

        if context:
            study_prompt = study_prompt + "Study material:\n" + context + "\n\n"

        study_prompt = study_prompt + "Question: " + original_prompt

        user_message = {"role": "user", "content": original_prompt}
        st.session_state.messages.append(user_message)
        st.chat_message("user").write(original_prompt)

        ollama_messages = st.session_state.messages.copy()
        ollama_messages[-1] = {"role": "user", "content": study_prompt}

        reply = ask_ollama(ollama_messages, model_name)

        assistant_message = {"role": "assistant", "content": reply}
        st.session_state.messages.append(assistant_message)
        st.chat_message("assistant").write(reply)
