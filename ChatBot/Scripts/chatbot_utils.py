from Scripts.vectordb_retriever import vector_retriever
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_community.llms import LlamaCpp
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline, GenerationConfig
from langchain import HuggingFacePipeline
import os

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

def load_llama2_7b():
    generation_config = GenerationConfig.from_pretrained("Models/Llama-2-7b-chat-hf")
    generation_config.max_new_tokens = 2000
    generation_config.temperature = 0.01
    generation_config.top_p = 1
    generation_config.repetition_penalty = 1.15
    
    tokenizer = AutoTokenizer.from_pretrained("Models/Llama-2-7b-chat-hf")
    model = AutoModelForCausalLM.from_pretrained("Models/Llama-2-7b-chat-hf")
    text_pipeline = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        return_full_text=True,
        generation_config=generation_config,
    )
    llm = HuggingFacePipeline(pipeline=text_pipeline,model_kwargs={"temperature":0.01})
    
    return llm

def load_retriever():
    retrieverObj = vector_retriever()
    db = retrieverObj.load_db()
    retriever = db.as_retriever()
    return retriever
# search_type="similarity_score_threshold",search_kwargs={"score_threshold": 0.5}