from Scripts.vectordb_retriever import vector_retriever
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.llms import LlamaCpp
import os
from transformers import AutoModel

def load_gpt():
    load_dotenv()
    OPENAI_API_KEY = os.environ["OPENAI_API_KEY"]
    llm = ChatOpenAI(model="gpt-3.5-turbo",
                     temperature=0.1,
                     max_tokens = 2000,
                     model_kwargs={"top_p": 0.9}
                     )
    return llm

def load_llama2_7b_q4():
    llm = LlamaCpp(
    model_path="Models/llama-7b-chat-q4/llama-2-7b-chat.Q4_0.gguf",
    temperature=0.01,
    max_tokens=2000,
    top_p=1,
    # callback_manager=callback_manager,
    verbose=False,  # Verbose is required to pass to the callback manager
    n_ctx = 2048,
    )
    
    return llm

def load_mistral_7b_q4():
    llm = LlamaCpp(
    model_path="Models/mistral-7b-q4/mistral-7b-instruct-v0.2.Q4_0.gguf",
    temperature=0.01,
    max_tokens=2000,
    top_p=1,
    # callback_manager=callback_manager,
    verbose=False,  # Verbose is required to pass to the callback manager
    n_ctx = 2048,
    )
    print("mistral hello")
    return llm

def load_falcon_7b_q4():
    llm = LlamaCpp(
    model_path="Models/falcon-7b-q4/tiiuae-falcon-7b-instruct-Q4_K_S.gguf",
    temperature=0.01,
    max_tokens=2000,
    top_p=1,
    # callback_manager=callback_manager,
    verbose=False,  # Verbose is required to pass to the callback manager
    n_ctx = 2048,
    )

    return llm

def load_orca_mini_7b_q4():
    llm = LlamaCpp(
    model_path="Models/orca-mini-7b-q4/orca_mini_v3_7b.Q4_0.gguf",
    temperature=0.01,
    max_tokens=2000,
    top_p=1,
    # callback_manager=callback_manager,
    verbose=False,  # Verbose is required to pass to the callback manager
    n_ctx = 2048,
    )
    
    return llm

def load_bloom_560m_q4():
    llm = LlamaCpp(
    model_path="Models/bloom-560m-q4/bloom-560m.q4_k_m.gguf",
    temperature=0.01,
    max_tokens=2000,
    top_p=1,
    # callback_manager=callback_manager,
    verbose=False,  # Verbose is required to pass to the callback manager
    n_ctx = 2048,
    )
    
    return llm

def load_llama3_8b_q4():
    llm = LlamaCpp(
    model_path="Models/llama-3-8b-q4/Meta-Llama-3-8B-Instruct.Q4_K_S.gguf",
    temperature=0.01,
    max_tokens=2000,
    top_p=1,
    # callback_manager=callback_manager,
    verbose=False,  # Verbose is required to pass to the callback manager
    n_ctx = 2048,
    )

    return llm

def load_retriever():
    retrieverObj = vector_retriever()
    db = retrieverObj.load_db()
    retriever = db.as_retriever(search_type="similarity_score_threshold",search_kwargs={"score_threshold": 0.5, 'k':10})
    return retriever