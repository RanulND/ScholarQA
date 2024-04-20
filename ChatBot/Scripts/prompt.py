from langchain.prompts import PromptTemplate
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains import create_history_aware_retriever
from Scripts.chatbot_utils import load_retriever


retriever = load_retriever()

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

# define system message

llm_prompt = """You are ScholarQA.\
        You are a helpful assistant for researchers who are querying computer science literature on large language models(LLMs).\
            Use only the following pieces of retrieved context to say yes or no to the question. Please do not make assumptions.\
                If you don't know the answer, just say that you don't know.
                
    {context} 
    """
    
quantum_prompt = """You are ScholarQA.\
        You are a helpful assistant for researchers who are querying computer science literature on quantum computing.\
            Use only the following pieces of retrieved context to answer the question. Please do not make assumptions.\
                If you don't know the answer, just say that you don't know. Keep the answer concise.
                
    {context} 
    """

def get_prompt_template_2(llm):


    ### Contextualize question ###
    contextualize_question = """Given a chat history and the latest user question which might reference context in the chat history,\
        formulate a standalone question which can be understood without the chat history. Do NOT answer the question,\
            just reformulate it if needed and otherwise return it as is."""
    
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
    qa_system_prompt = llm_prompt
    
    qa_prompt = ChatPromptTemplate.from_messages(
        [
            ("system", qa_system_prompt),
            MessagesPlaceholder("chat_history"),
            ("human", "{input}"),
        ]
    )

    return history_aware_retriever, qa_prompt


