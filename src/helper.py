from hugchat import hugchat
from hugchat.login import Login

def login(email: str, password: str) -> hugchat.RequestsCookieJar:
    """
    Logs in the user with the provided email and password.

    Parameters:
        email (str): The email address of the user.
        password (str): The password associated with the email address.

    Returns:
        hugchat.RequestsCookieJar: A cookie jar containing the authentication cookies
        obtained after successful login.

    Raises:
        LoginError: If the login process fails due to invalid credentials or other reasons.
    """
    credentials = Login(email, password)
    cookies = credentials.login()

    # save cookies
    cookies_path_dir = './cookies_snapshot'
    credentials.saveCookiesToDir(cookies_path_dir)
    
    return cookies
    

def chatbot(cookies: hugchat.RequestsCookieJar) -> hugchat.ChatBot:
    """
    Creates a new instance of the chatbot using the provided credentials and cookies.

    Parameters:
        email (str): The email address used for authentication.
        password (str): The password associated with the email address.
        cookies (hugchat.RequestsCookieJar): A cookie jar containing authentication cookies.

    Returns:
        hugchat.ChatBot: An instance of the chatbot initialized with the provided cookies
        and default language model.

    Note:
        The function initializes the chatbot with a default language model "mistralai/Mixtral-8x7B-Instruct-v0.1".
        It also creates a new conversation within the chatbot instance.

    Raises:
        Any exceptions raised during the initialization of the chatbot instance.
    """
    # create the chatbot instance
    default_llm = "mistralai/Mixtral-8x7B-Instruct-v0.1"
    chatbot = hugchat.ChatBot(cookies=cookies.get_dict(), default_llm=default_llm)

    # create new conversation
    id = chatbot.new_conversation()
    chatbot.change_conversation(id)

    return chatbot

if __name__ == "__main__":
    pass