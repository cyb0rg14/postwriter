from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

groq_api_key = "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"

model_name = "mixtral-8x7b-32768"
chat = ChatGroq(model_name=model_name, groq_api_key=groq_api_key)

system = "You are an expert Social Media Writer. You know how to write posts that are engaging and informative."

human = "{text}"

prompt = PromptTemplate(
    input_variables=["text"],
    template= system + human,
)

chain = prompt | chat
output = chain.invoke({"text": "Help me write a twitter post on 'Explaining general relativity'"})
output.content