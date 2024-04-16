import streamlit as st
from hugchat import hugchat
from helper import login, chatbot

def write_post(chatbot: hugchat.ChatBot, message: str) -> None:
    prompt = f"""
        Write a linkedin post on the topic: {message}
    """
    response = chatbot.chat(prompt)
    return response['text']


email = st.secrets['email']
password = st.secrets['password']

cookies = login(email, password)
chatbot = chatbot(cookies)

print(write_post(chatbot, 'Reinforcemnent Learning 101'))