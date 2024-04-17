# page configuration variables
page_title = "Post Writer"
favicon = "./assets/postwriter-cc.png"
menu_items = {
    "About": "https://github.com/cyb0rg14/PostWriter",
    "Report a bug": "https://github.com/cyb0rg14/PostWriter/issues",
    "Get help": "mailto:cyborgdomain@proton.me"
}

# main varaibles
banner = "./assets/postwriter-logo.png"
header = ":blue[Your Personal Bot] for Better :green[Social Media Post]"

# configuration variables
social_medias = ["Twitter", "LinkedIn", "Reddit", "Instagram", "Other"]

tones = ['Professional', 'Friendly', 'Conversational', 'Humurous', 'Educational', 'Inspirational', 'Authentic']

templates = [
    "I would like to have a new post about given topic!",
    "I would like to customize my draft!",
]

title_template= "ex: Reinforcement Learning 101"
draft_template = """ex: Delving into the mind-bending world of #generalrelativity! 🤯 Einstein\'s groundbreaking theory explains how gravity is a warping of space and time by mass. Imagine a bowling ball on a trampoline; that\'s our planet in the universe\'s fabric! 🌎⚽️ #scitech #space"""

# writer variables
model_name = "mixtral-8x7b-32768"

system_prompt="You're a skilled Social Media Writer, adept at creating engaging and informative posts across diverse topics. Your aim is to captivate your audience, spark discussions, and provide value. Maintain a {tone} tone while delivering accurate and insightful content. Your posts should leave readers eager to engage and return for more."

on_topic="Today, assist me in crafting a {social_media} post about '{topic}'. Let's aim for a post length of around {number_of_words} words."
customize_draft="Today, assist me in crafting a {social_media} post by customizing the following draft {draft}. Let's aim for a post length of around {number_of_words} words."

human_prompt = {
    "on_topic": on_topic,
    "customize_draft": customize_draft
}
