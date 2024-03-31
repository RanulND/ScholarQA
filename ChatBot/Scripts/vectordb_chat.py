from langchain.chains import RetrievalQA
from Scripts.prompt import get_prompt_template_2
from Scripts.chatbot_utils import load_llm,load_retriever

# load the llm
def chat_with_vectordb():
    llm = load_llm()

    retriever = load_retriever()
    prompt,memory = get_prompt_template_2()

    retrieval_chain = RetrievalQA.from_chain_type(llm,
                                                chain_type="stuff",
                                                retriever=retriever,
                                                chain_type_kwargs={
                                                    "prompt": prompt,
                                                    "memory": memory
                                                },
                                                )
    return retrieval_chain
