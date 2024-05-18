import sys
sys.path.append("../../Chatbot")
import os
from langchain_community.graphs import Neo4jGraph
from langchain_experimental.graph_transformers import LLMGraphTransformer
from ChatBot.Scripts.chatbot_utils import load_gpt
from langchain_core.documents import Document
import json

def init_neo4j():
    graph = Neo4jGraph()
    return graph

def init_graph_transformer():
    llm_transformer = LLMGraphTransformer(llm=load_gpt())
    return llm_transformer

def convert_docs_to_graph():
    json_folder = "Sample Files/json format"
    json_files = [f"{json_folder}/{file}" for file in os.listdir(json_folder) if file.endswith('.json')]
    graph_db = init_neo4j()
    llm_transformer = init_graph_transformer()
    documents = []
    for json_file in json_files:
        with open(json_file, 'r') as f:
            data = json.load(f)
            abstract = data.get('Abstract', '')
            documents.append(Document(page_content=abstract))
            
    graph_documents = llm_transformer.convert_to_graph_documents(documents)
    graph_db.add_graph_documents(graph_documents)


