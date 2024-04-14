from langchain.chains import ConversationalRetrievalChain
from Scripts.prompt import get_prompt_template_2
from Scripts.chatbot_utils import load_llm,load_retriever
from langchain.memory import ConversationBufferMemory
from langchain.chains import RetrievalQA


# load the llm
def chat_with_vectordb():
    llm = load_llm()

    retriever = load_retriever()
    prompt = get_prompt_template_2()
    memory = ConversationBufferMemory(input_key='question', memory_key='chat_history', k=5, return_messages=True)

    retrieval_chain = RetrievalQA.from_chain_type(llm,
                                                chain_type="stuff",
                                                retriever=retriever,
                                                chain_type_kwargs={
                                                    "memory":memory,
                                                    "prompt": prompt
                                                }
                                                )
    return retrieval_chain