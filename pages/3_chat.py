import streamlit as st
import ollama as ol
import pandas as pd

try:
    st.sidebar.title("Old Chats")

    conversation_df = pd.read_csv("Database.csv")

    chat_ids = conversation_df["chat_id"].unique()

    for chat_id in chat_ids:

        if st.sidebar.button(f"Chat {chat_id}"):

            selected_chat = conversation_df[
                conversation_df["chat_id"] == chat_id
            ]

            selected_chat = selected_chat.drop(columns=["chat_id"])

            st.session_state.messages = selected_chat.to_dict(
                orient="records"
            )

            st.session_state.chat_id = chat_id

except FileNotFoundError:
    st.sidebar.write("No previous chats found.")

if st.button("New Chat"):
    conversation_df=pd.DataFrame(st.session_state.messages)
    conversation_df["chat_id"] = st.session_state.chat_id
    conversation_df.to_csv("Database.csv", mode='a', index=False, header=False)
    st.session_state.chat_id += 1
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! Ask me anything about your studies."
        }
    ]

if "chat_id" not in st.session_state:
    st.session_state.chat_id = 1


def ask_llama(messages):
    response = ol.chat(
        model="qwen3",
        messages=messages
    )

    return response["message"]["content"]


st.title("AI Study Chat")

if "messages" not in st.session_state:
    st.session_state.chat_id += 1
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hello! Ask me anything about your studies."
        }
    ]


for message in st.session_state.messages:
    st.chat_message(message["role"]).write(message["content"])


prompt = st.chat_input("Ask anything...")


if prompt:
    user_message = {
        "role": "user",
        "content": prompt
    }

    st.session_state.messages.append(user_message)
    st.chat_message("user").write(prompt)

    reply = ask_llama(st.session_state.messages)

    assistant_message = {
        "role": "assistant",
        "content": reply
    }

    st.session_state.messages.append(assistant_message)
    st.chat_message("assistant").write(reply)