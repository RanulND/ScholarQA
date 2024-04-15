from Scripts.vectordb_chat import chat_with_vectordb
from Scripts.hybrid_chat import chat_hybrid
from dotenv import load_dotenv
import os

# get the vector db chat
def runme_vector():
    load_dotenv()
    LANGCHAIN_TRACING_V2 = os.getenv('LANGCHAIN_TRACING_V2')
    LANGCHAIN_ENDPOINT = os.getenv('LANGCHAIN_ENDPOINT')
    LANGCHAIN_API_KEY = os.getenv('LANGCHAIN_API_KEY')
    LANGCHAIN_PROJECT = os.getenv('LANGCHAIN_PROJECT')
    
    retrieval_chain = chat_with_vectordb()

    while True:
        query = input("You: ")
        
        if query.lower() == "exit":
            print("Exiting the chat session. Have a nice day!")
            break
        
        answer = retrieval_chain.invoke({"input": query},
        config={
            "configurable": {"session_id": "abc123"}
            },  # constructs a key "abc123" in `store`.
        )["answer"]
        print(answer)

# to get the hybrid chat
def runme_hybrid():
    dialogue = chat_hybrid()
    return dialogue


# function call for vector chat
runme_vector()

# function call for hybrid chat
# runme_hybrid()