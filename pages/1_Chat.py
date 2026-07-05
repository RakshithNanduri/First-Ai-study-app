import streamlit as st
import ollama as ol


def ask_ollama(messages):
    response = ol.chat(model="qwen3:latest", messages=messages)
    answer = response["message"]["content"]
    return answer


if "messages" not in st.session_state:
    st.session_state.messages = [
        {
            "role": "assistant",
            "content": "Hey! How can I help you?"
        }
    ]


for message in st.session_state.messages:
    role = message["role"]
    content = message["content"]

    st.chat_message(role).write(content)


prompt = st.chat_input("Ask me anything")


if prompt:
    user_message = {
        "role": "user",
        "content": prompt
    }

    st.session_state.messages.append(user_message)

    st.chat_message("user").write(prompt)

    reply = ask_ollama(st.session_state.messages)

    assistant_message = {
        "role": "assistant",
        "content": reply
    }

    st.session_state.messages.append(assistant_message)

    st.chat_message("assistant").write(reply)