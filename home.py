from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI


llm= ChatOpenAI(
    model = 'gpt-3.5-turbo',
    temperature=0.8,
    max_tokens =1000,
    verbose= True
)

response = llm.invoke('Shalom. how are you? ')
print(response)