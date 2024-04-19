from Scripts.prompt import get_prompt_template_1
from Scripts.chatbot_utils import load_gpt,load_retriever
from langchain.chains import LLMChain



def chat_hybrid():
    llm = load_gpt() # load the llm
    prompt = get_prompt_template_1()
    db = load_retriever()
    chain = LLMChain(llm=llm, prompt=prompt)
    
    question = input("ScholarQA: Enter your question\n")
    
    candidate_1 = db.get_relevant_documents(question) # look for symantix retreival 
    #https://python.langchain.com/docs/modules/data_connection/retrievers/self_query/
    candidate_2 = input("ScholarQA: Enter KG data\n")

    hybrid_answer = chain.run(question=question,
                                candidate_1=candidate_1,
                                candidate_2=candidate_2)
    
    print("ScholarQA: ", hybrid_answer)
