from langchain.memory import ConversationBufferMemory
from langchain.prompts import PromptTemplate

# define system message
system_prompt = """ You are ScholarQA. You are a helpful assistant for the researchers to query scientific literature on 
large language models also known as llms. You will use the provided answer candidates to answer user questions. 
There will be two answer candidates, CANDIDATE_1 and CANDIDATE_2. CANDIDATE_1 is a list, and CANDIDATE_2 is a list of dictionaries. 
Each item in the list represents one potential answer. But their relevance for the user question is not guranteed. So please be mindful
 and generate the best-detailed answer for the question. The generated answer can be a combination of both the answer candidates. 
 If none of the answer candidates makes sense, or the information is not enough to answer the question, please do not make assumptions. 
 Just tell the user that the provided information is insufficient to generate a quality answer.
"""

def get_prompt_template(system_prompt=system_prompt):

    B_INST, E_INST = "[INST]", '[/INST]'

    B_SYS  , E_SYS = "<<SYS>>\n" , "\n<</SYS>>\n\n"

    SYSTEM_PROMPT = B_SYS + system_prompt + E_SYS

    instructions = """
    ---------------------------
    CANDIDATE_1: {candidate_1}
    CANDIDATE_2: {candidate_2}
    ---------------------------
    HISTORY: {history}
    ---------------------------
    QUESTION: {question}
    ---------------------------
    Answer: 
    """

    prompt_template = B_INST + SYSTEM_PROMPT + instructions + E_INST

    prompt = PromptTemplate(input_variables=['history','candidate_1','candidate_2','question'], template=prompt_template)

    memory = ConversationBufferMemory(input_key='question', memory_key='history', k=5, return_messages=True)

    return (
        prompt,
        memory
    )

