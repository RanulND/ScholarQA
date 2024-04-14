from langchain.chains import ConversationalRetrievalChain
from Scripts.prompt import get_prompt_template_2
from Scripts.chatbot_utils import load_llm,load_retriever
from langchain.memory import ConversationBufferMemory


# load the llm
def chat_with_vectordb():
    llm = load_llm()

    retriever = load_retriever()
    prompt = get_prompt_template_2()
    memory = ConversationBufferMemory(input_key='question', memory_key='history', k=5, return_messages=True)

    retrieval_chain = ConversationalRetrievalChain.from_llm(llm,
                                                #chain_type="stuff",
                                                memory=memory,
                                                retriever=retriever,
                                                combine_docs_chain_kwargs={
                                                    "prompt": prompt
                                                },
                                                get_chat_history=lambda h: h,
                                                )
    return retrieval_chain