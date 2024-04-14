from langchain.prompts import PromptTemplate



def get_prompt_template_1():

    # define system message
    system_prompt_1 = """ You are ScholarQA. You are a helpful assistant for the researchers to query scientific literature on large language models also known as llms. You will use the provided answer candidates; candidate_1 and candidate_2 to answer the question. 
    Be mindful and construct the  answer to the question that responds with the highest degree of confidence and most attention to detail. 
    If none of the answer candidates makes sense, or the information is not enough to answer the question, please do not make assumptions. 
    Just tell the user that the provided information is insufficient to generate a quality answer.
    """

    B_INST, E_INST = "[INST]", '[/INST]'

    B_SYS  , E_SYS = "<<SYS>>\n" , "\n<</SYS>>\n\n"

    SYSTEM_PROMPT = B_SYS + system_prompt_1 + E_SYS

    instructions = """
    ---------------------------
    CANDIDATE_1: {candidate_1}
    ---------------------------
    CANDIDATE_2: {candidate_2}
    ---------------------------
    QUESTION: {question}
    ---------------------------
    Answer: 
    """

    prompt_template = B_INST + SYSTEM_PROMPT + instructions + E_INST

    prompt = PromptTemplate(input_variables=['candidate_1','candidate_2','question'], template=prompt_template)

    return prompt

# define system message

def get_prompt_template_2():

    system_prompt_2 = """ 
    You are ScholarQA. You are a helpful assistant for the researchers to query scientific literature on large language models (llms). 
    Use only the following context (delimited by <ctx></ctx>) and the chat history (delimited by <hs></hs>) to answer the question. 
    Please do not make assumptions. If you don't know the answer tell the user that you don't have enough information to answer.
        ------
        <ctx>
        {context}
        </ctx>
        ------
        <hs>
        {history}
        </hs>
        ------
        {question}
        Answer:
    """
 

    prompt_template = system_prompt_2

    prompt = PromptTemplate(
    input_variables=["context", "question", "history"],
    template=prompt_template,
    )

    return prompt
