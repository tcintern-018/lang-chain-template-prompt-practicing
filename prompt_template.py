from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq

load_dotenv()

llm = ChatGroq(model="llama-3.3-70b-versatile")

template = PromptTemplate.from_template(
     "Explain {topic} like I am 10 years old."
)

prompt = template.invoke(
    {
        "topic": "Machine Learning"
    }
)

response = llm.invoke(prompt)

print(response.content)