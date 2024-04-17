# import all the required packages
import streamlit as st
from sidebar import sidebar_conf
from writer import write_post
from constants import *

# set the page configuration
st.set_page_config(
    page_title=page_title,
    page_icon=favicon,
    layout="centered",
    initial_sidebar_state="expanded",
    menu_items=menu_items
)

# configure sidebar
sidebar_conf()

# style the header
st.header(header, divider="rainbow")

# social media
social_media = st.selectbox(
    "select the social media platform",
    social_medias
)

if social_media == "Other":
    social_media = st.text_input("Enter the social media platform:", placeholder="ex: twitter")

# number of words
col1, col2 = st.columns([2, 3])
with col1:
    tone = st.selectbox(
        "select the tone",
        tones
    )
with col2:
    number_of_words = st.slider("select the number of words", min_value=30, max_value=500, value=120, step=10)

# premade template
template = st.selectbox(
    "how you would like to start?",
    templates
)

if 'title' in template:
    title = st.text_input("Enter the title:", placeholder=title_template)
elif 'draft' in template: 
    text_input = st.text_area("Enter the Draft:", placeholder=draft_template)


# generate output
user_inputs = {
    "social_media": social_media,
    "number_of_words": number_of_words,
    "tone": tone,
    "on_topic": title
}

groq_api_key = st.secrets['groq_api_key']
response = write_post(user_inputs, groq_api_key)

st.text_area("Your Post:", value=response)
