import os
from langchain.llms import OpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

# Define your prompt template
prompt = PromptTemplate(input_variables=["question"], template="What is {question}?")

# Initialize the LLM with OpenAI API
api_key = os.getenv('OPENAI_API_KEY')
llm = OpenAI(api_key=api_key)
chain = LLMChain(llm=llm, prompt=prompt)

# Run the chain
response = chain.run("the capital of France")
print(response)
