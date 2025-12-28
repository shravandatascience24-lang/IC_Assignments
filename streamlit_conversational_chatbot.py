from openai import OpenAI
import streamlit as st


# Initialize OpenAI client

st.title("💬 AI Powered Chatbot ")
st.code("An interactive chatbot using Streamlit and OpenAI's GPT-5.2 model.")
if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "system", "content": "How can I help you?"}]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():

    client = OpenAI(api_key="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")
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    response = client.chat.completions.create(model="gpt-5.2", messages=st.session_state.messages)
    msg = response.choices[0].message.content
    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)