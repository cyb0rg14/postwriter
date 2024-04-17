import streamlit as st
from constants import *

heading = "### The only bot you need to write the most engaging social media posts!"

def sidebar_conf():
    st.sidebar.image(banner)
    st.sidebar.markdown(heading)


if __name__ == "__main__":
    sidebar_conf()