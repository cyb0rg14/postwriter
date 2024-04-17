import streamlit as st
from constants import *

heading = "> ## The only bot you need to write the most engaging social media posts!"

# instructions variable
instructions = """
# *Getting the most out of it:*
- **Select Your Platform**: Choose the social media platform that suits your needs. If it's not listed, select "Other"

- **Set the Tone** : Decide how you want your post to be perceived by choosing the appropriate tone.

- **Adjust Post Duration**: Customize the lifespan of your post according to your preferences.

- **Craft Your Topic**: Write about anything that interests you or relates to your project.
"""
topic_info = """
**example 1**: I want to showcase my new project `PostWriter` which writes content for your social media within few clicks.\n
**example 2**: Step by step approach for a newbie to learn Reinforcement Learning in 30 days. 
"""

# draft variables
draft_instruction = "- **Customize Your Predbuilt Draft**: Alternatively, you can also tailor your pre-built draft to better fit your needs."
draft_info = f"**example**: {draft_template[3:]}"

# post instructions
post_instruction = """
## *And Hooray! Your dish is ready*
You could **copy it to clipboard** and share it with your audience.
"""

# post message
post_message= """
## For any kind of problem:
You could open an issue at this [repo](https://github.com/cyb0rg14/PostWriter/issues) or connect with me on [LinkedIn](https://www.linkedin.com/in/cyb0rg14/)
"""

# other projects
other_projects = """
### My Other Projects:
- 🕵🏻‍♂️ [StatEase](https://statease.streamlit.app)
- 👻 [AnimeOdyssey](https://animeodysseyy.streamlit.app)
- 🗺️ [WallFindr](https://wallfindr.streamlit.app)
- 📜 [ArtiFact](https://artifact.streamlit.app)
- 🦙 [ChatBot](https://chatbotmaven.streamlit.app)

# Made with :heart: by [cyb0rg14](https://github.com/cyb0rg14)
"""

def sidebar_conf():
    sidebar = st.sidebar

    # upper heading
    sidebar.image(banner)
    sidebar.markdown(heading)
    sidebar.divider()

    # instructions
    sidebar.markdown(instructions)
    sidebar.info(topic_info)
    sidebar.markdown(draft_instruction)
    sidebar.info(draft_info)
    sidebar.markdown(post_instruction)
    sidebar.divider()

    # post message
    sidebar.markdown(post_message)
    sidebar.divider()

    # other projects
    sidebar.markdown(other_projects)

if __name__ == "__main__":
    sidebar_conf()