from dotenv import dotenv_values
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI


config = dotenv_values(".env")

system_template = "Translate the following into {language}:"
user_template= "{text}"
prompt_template = ChatPromptTemplate.from_messages(
    [("system", system_template), ("user", user_template)]
)

print(prompt_template)

api_key = config["OPENAI_API_KEY"]
modelName = config["OPENAI_MODEL_NAME"]
model = ChatOpenAI(model=modelName, openai_api_key=api_key)

parser = StrOutputParser()

llm = prompt_template | model | parser

# response = llm.invoke({"language": "italian", "text": "Hello, World!"})
# print(response)
