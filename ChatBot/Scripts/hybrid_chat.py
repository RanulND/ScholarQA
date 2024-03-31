from Scripts.prompt import get_prompt_template_1
from Scripts.chatbot_utils import load_llm,load_retriever
from langchain.chains import LLMChain



def chat_hybrid():
    question = input("ScholarQA: Enter your question")
    llm = load_llm() # load the llm
    prompt = get_prompt_template_1()
    db = load_retriever()

    chain = LLMChain(llm=llm, prompt=prompt)
    candidate_1 = db.get_relevant_documents(question)
    candidate_2 = input("ScholarQA: Enter KG data")

    hybrid_answer = chain.run(question=question,
                                candidate_1=candidate_1,
                                candidate_2=candidate_2)
    
    print("ScholarQA: ", hybrid_answer)
