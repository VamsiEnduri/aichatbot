import streamlit as st 
from openai import OpenAI
from dotenv import dotenv_values


config = dotenv_values(".env")

# print(config)

client = OpenAI(
    api_key=config["open_api_key"],
    base_url="https://api.groq.com/openai/v1"
)

# print(client,"client")

# title
st.title("Ai chatbot")

if "messages" not in st.session_state:
    st.session_state.messages=[]
# st.sidebar.header("choose role ")

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])


user_input = st.chat_input("Type message...")

if user_input:
    st.session_state.messages.append({
        "role":"user",
        "content":user_input
    })

    with st.chat_message("user"):
        st.write(user_input)


    with st.chat_message("assistant"):
        with st.spinner("thinking"):
            response=client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=st.session_state.messages
            ) 
            # print(response) 
            reply=response.choices[0].message.content 
            st.write(reply)


    st.session_state.messages.append({
        "role":"assistant",
        "content":reply
    })        
