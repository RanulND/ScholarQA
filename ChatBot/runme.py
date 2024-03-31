from Scripts.vectordb_chat import chat_with_vectordb
from Scripts.hybrid_chat import chat_hybrid

# get the vector db chat
def runme_vector():
    retrieval_chain = chat_with_vectordb()

    while True:
        query = input("You: ")
        
        if query.lower() == "exit":
            print("Exiting the chat session. Have a nice day!")
            break
        
        answer = retrieval_chain.invoke(query)
        result = answer['result'] 
        print("ScholarQA:", result)

# to get the hybrid chat
def runme_hybrid():
    dialogue = chat_hybrid()
    return dialogue


# function call for vector chat
runme_vector()

# function call for hybrid chat
# runme_hybrid()