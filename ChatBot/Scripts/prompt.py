from langchain.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import create_history_aware_retriever
from Scripts.chatbot_utils import load_retriever


retriever = load_retriever()

# follow the below template format if you use Mistral of Falcon
# <s>[INST] Instruction [/INST] Model answer</s>[INST] Follow-up instruction [/INST]   

# define system messages; first phase

# for LLM questions
llm_prompt = """You are ScholarQA.\
        You are a helpful assistant for researchers who are querying computer science literature on large language models(LLMs).\
            Use only the following pieces of retrieved context to answer the question. Please do not make assumptions.\
                The questions expect yes/no as the answer. So your answer should be either yes/no.\
                    But if you don't know the answer, just say that you don't know.
                
    {context} 
    """
    
# for edge computing questions    
edge_prompt = """You are ScholarQA.\
        You are a helpful assistant for researchers who are querying computer science literature on edge computing.\
            Use only the following pieces of retrieved context to answer the question. Please do not make assumptions.\
                The questions expect yes/no as the answer. So your answer should be either yes/no.\
                    But if you don't know the answer, just say that you don't know.
                
    {context} 
    """

# for quantum computing questions    
quantum_prompt = """You are ScholarQA.\
        You are a helpful assistant for researchers who are querying computer science literature on quantum computing.\
            Use only the following pieces of retrieved context to answer the question. Please do not make assumptions.\
                If you don't know the answer, just say that you don't know. Keep the answer concise.
                
    {context} 
    """

### Contextualize question ###
contextualize_question = """Given a chat history and the latest user question which might reference context in the chat history,\
    formulate a standalone question which can be understood without the chat history. Do NOT answer the question,\
        just reformulate it if needed and otherwise return it as is."""
        

# prompts for mistral llm
mistral_llm_prompt = """<s>[INST] You are a helpful assistant for researchers who are querying computer science literature on large language modelling(LLM).\
    Use only the following pieces of retrieved context to answer the question. Please do not make assumptions.\
    These are binary questions. So your answer should be either yes/no. But if you don't know the answer, \
    just say that you don't know. 
    {context} [/INST] \
    Model answer: </s>
"""

mistral_edge_prompt = """<s>[INST] You are a helpful assistant for researchers who are querying computer science literature on edge computing.\
    Use only the following pieces of retrieved context to answer the question. Please do not make assumptions.\
    These are binary questions. So your answer should be either yes/no. But if you don't know the answer, \
    just say that you don't know. 
    {context} [/INST] \
    Model answer: </s>
"""

### Contextualize question - Mistral ###
contextualize_mistral_question = """<s>[INST] Given a chat history and the latest user question which might reference context in the chat history,\
    formulate a standalone question which can be understood without the chat history. Do NOT answer the question,\
        just reformulate it if needed and otherwise return it as is. [/INST] </s>
"""

def get_prompt_template_2(llm):
    
    contextualize_q_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", contextualize_question),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )
    history_aware_retriever = create_history_aware_retriever(
        llm, retriever, contextualize_q_prompt
    )


    ### Answer question ###
    qa_system_prompt = mistral_edge_prompt
    
    qa_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", qa_system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )

    return history_aware_retriever, qa_prompt



# define system messages; second phase


def get_prompt_template_1():

    # define system message
    system_prompt_1 = """ You are ScholarQA.\
        You are a helpful assistant for the researchers to query scientific literature on large language models also known as llms.\
            You will use the provided answer candidates; candidate_1 and candidate_2 to answer the question.\
                Be mindful and construct the  answer to the question that responds with the highest degree of confidence and most attention to detail.\
                    If none of the answer candidates makes sense, or the information is not enough to answer the question, please do not make assumptions.\
                        Just tell the user that the provided information is insufficient to generate a quality answer.

    ---------------------------
    CANDIDATE_1: {candidate_1}
    ---------------------------
    CANDIDATE_2: {candidate_2}
    ---------------------------
    QUESTION: {question}
    ---------------------------
    Answer: 
    """

    prompt = PromptTemplate(input_variables=['candidate_1','candidate_2','question'], template=system_prompt_1)

    return prompt
