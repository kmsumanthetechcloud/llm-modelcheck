from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain.chat_models import ChatOpenAI
from langchain_community.chat_models import ChatOpenAI
from langserve import add_routes
from fastapi import FastAPI
import uvicorn
from langchain_community.llms import Ollama
from dotenv import load_dotenv

import os

load_dotenv()
os.environ["OPENAI_API_KEY"]=os.getenv("OPENAI_API_KEY")

app=FastAPI(

    title="Langchain Server",
    version="1.0",
    description="A Simple API Server"
)


add_routes(
    app,
    ChatOpenAI(),
    path="/openai"

)
#model=ChatPromptTemplate("your prompt string")
model = ChatPromptTemplate.from_template("your prompt string")## ollama llm model
llm=Ollama(model="gemma3:1b")

prompt1=ChatPromptTemplate.from_template("write me an essay about {topic} with 20 words")
prompt2=ChatPromptTemplate.from_template("write me an poem about {topic} for a five year girl")


add_routes(
    app,
    prompt1|model,
    path="/essay"


)


add_routes(
    app,
    prompt2|llm,
    path="/poem"
)

if __name__=="__main__":
    uvicorn.run(app,host="localhost",port=8000)







