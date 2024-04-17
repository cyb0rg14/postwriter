from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq 
from constants import system_prompt, human_prompt


def write_post(user_inputs: dict, api_key: str) -> str:
    model_name = "mixtral-8x7b-32768"
    chatbot = ChatGroq(model_name=model_name, groq_api_key=api_key)
    prompt = PromptTemplate(
        input_variables=["social_media", "tone", "number_of_words", "topic"],
        template=system_prompt+human_prompt['on_topic'],
    )
    chain = prompt | chatbot
    output = chain.invoke({
        "social_media": user_inputs["social_media"],
        "tone": user_inputs["tone"],
        "number_of_words": user_inputs["number_of_words"],
        "topic": user_inputs["on_topic"]
    })
    return output.content


if __name__ == "__main__":
    pass