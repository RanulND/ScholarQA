from Scripts.vectordb_retriever import vector_retriever
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os

def load_llm():
    load_dotenv()
    OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
    llm = ChatOpenAI(model="gpt-3.5-turbo",
                     temperature=0.1,
                     max_tokens = 2000,
                     model_kwargs={"top_p": 0.9}
                     )
    return llm

def load_retriever():
    retrieverObj = vector_retriever()
    db = retrieverObj.load_db()
    retriever = db.as_retriever()
    return retriever
# search_type="similarity_score_threshold",search_kwargs={"score_threshold": 0.5}