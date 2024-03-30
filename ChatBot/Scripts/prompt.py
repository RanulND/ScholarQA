from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate


"""
this is the prompt to be used for the hybrid approach which uses both the vector db and knowledge graphs for answer generation.
"""


def get_prompt_template_1():

    # define system message
    system_prompt_1 = """ You are ScholarQA. You are a helpful assistant for the researchers to query scientific literature on 
    large language models also known as llms. You will use the provided answer candidates to answer user questions. 
    There will be two lists answer candidates, candidate_1 and candidate_2. Each item in the list represents one potential answer. But their relevance for the user question is not guranteed. 
    So be mindful and construct the detailed answer to the question that responds with the highest degree of confidence and most attention to detail. 
    The generated answer can be from most ideal candidate or a combination of both the candidates. 
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


"""
this is the prompt to be used for querying vector db.
"""

# define system message

def get_prompt_template_2():

    system_prompt_2 = """ 
    You are ScholarQA. 
    You are a helpful assistant for the researchers to query scientific literature on large language models (llms). 
    You will answer the questions only using the context and the history. 
    Construct a detailed answer to the question that responds with the highest degree of confidence and most attention to detail. 
    If the context or the histroy is irrelevant to the question, please do not make assumptions. 
    Tell the user that the provided information is insufficient to generate a quality answer.
    """

    B_INST, E_INST = "[INST]", '[/INST]'

    B_SYS  , E_SYS = "<<SYS>>\n" , "\n<</SYS>>\n\n"

    SYSTEM_PROMPT = B_SYS + system_prompt_2 + E_SYS

    instructions = """
    ---------------------------
    CONTEXT: {context}
    ---------------------------
    HISTORY: {history}
    ---------------------------
    QUESTION: {question}
    ---------------------------
    Answer: 
    """

    prompt_template = B_INST + SYSTEM_PROMPT + instructions + E_INST

    prompt = PromptTemplate(input_variables=['context','history','question'], template=prompt_template)

    memory = ConversationBufferMemory(input_key='question', memory_key='history', k=5, return_messages=True)

    return (
        prompt,
        memory
    )

