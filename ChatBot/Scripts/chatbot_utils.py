from Scripts.vectordb_retriever import vector_retriever
from langchain_community.llms import LlamaCpp

def load_llm():
    llm = LlamaCpp(
    model_path="../Models/llama-7b-chat-q4/llama-2-7b-chat.Q4_0.gguf",
    temperature=0.75,
    max_tokens=2000,
    top_p=1,
    # callback_manager=callback_manager,
    verbose=True,  # Verbose is required to pass to the callback manager
    n_ctx = 2048
    )
    return llm

def load_retriever():
    retrieverObj = vector_retriever()
    db = retrieverObj.load_db()
    retriever = db.as_retriever(k=5)
    return retriever