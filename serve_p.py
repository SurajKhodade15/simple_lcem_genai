from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langserve import add_routes 
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv
load_dotenv()


groq_api_key = os.getenv("GROQ_API_KEY")
model = ChatGroq(model="llama-3.1-8b-instant", groq_api_key=groq_api_key)

system_template = "Translate the following text to: {language}"
prompt_template = ChatPromptTemplate.from_messages([
  ('user', "{text}"),
  ('system', system_template)
])

parser = StrOutputParser()

chain = prompt_template | model | parser
# Disable docs/OpenAPI to avoid Pydantic v2 issues
app = FastAPI(
    title="Langchain Server",
    version="1.0",
    description="A server for Langchain applications",
)
add_routes(app, chain, path="/chain")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
