from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()


llm= ChatOpenAI(
    temperature= 0.7,
    model='gpt-3.5-turbo-1106'
)

prompt = ChatPromptTemplate.from_template('Tell me a joke about {subject}.')

chain = prompt | llm

response = chain.invoke({'subject': 'dogs'})
print(response)
