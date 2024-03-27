from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings.sentence_transformer import (
    SentenceTransformerEmbeddings,
)
import json
import os
from langchain_community.vectorstores import FAISS

class DB:
    """
    This class is defined to store abstracts in a vector store.
    """
    def __init__(self, json_folder, vector_path="DataBase/VectorDB/vectorstore"):
        """
        Initializes the DB class to store abstracts in a vectore store.

        Args:
            json_folder (str): Path to the folder containing JSON files.
            vector_path (str): Path to the folder where vectorised abstracts will be saved
        
        Output:
            vector database
        """
        # Define chunk size, overlap and separators
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=512,
            chunk_overlap=10,
            separators=['\n\n', '. ']
        )

        self.json_folder = json_folder

        # specific for scientific literature
        self.embedding_model = "DataBase/VectorDB/embedding-allenai-specter"

        # store json files in a list
        self.json_files = [f"{json_folder}/{file}" for file in os.listdir(json_folder) if file.endswith('.json')]

        # Initialize an empty vector store
        self.vectorstore = None   

        self.vector_path = vector_path

    
    # Function for loading the embedding model
    def load_embedding_model(self, normalize_embedding=True):
        return SentenceTransformerEmbeddings(
            model_name= self.embedding_model,
            model_kwargs={'device':'cpu'}, # here we will run the model with CPU only
            encode_kwargs = {
                'normalize_embeddings': normalize_embedding # keep True to compute cosine similarity
            }
        )
    

    # Function for creating embeddings using FAISS
    def create_embeddings(self, chunks, embedding_model):
        embedding_model = self.load_embedding_model()
        if os.path.exists(self.vector_path+'/index.faiss'):
            vectorstore = FAISS.load_local(self.vector_path, embeddings=embedding_model,allow_dangerous_deserialization=True)
        else:
            vectorstore = FAISS.from_texts(chunks, embedding_model)
        
        # Saving the model in current directory
        vectorstore.save_local(self.vector_path)
        
        # returning the vectorstore
        return vectorstore
    

    #update the existing vector store
    def update_vectorstore(self,docs,meta_dict):
        # Load or create the embedding model
        embedding_model = self.load_embedding_model()
        
        # If vectorstore is None, initialize it with the first set of embeddings
        if self.vectorstore is None:
            self.vectorstore = self.create_embeddings(docs, embedding_model)

        else:
            # Update the vectorstore with new embeddings
            self.vectorstore.add_texts(docs, metadatas=[meta_dict] * len(docs), embeddings_model=embedding_model)
            
        # Save the updated vectorstore
        self.vectorstore.save_local(folder_path=self.vector_path)

    
    # process the json file to create embeddings and store in the vectore db
    def process_json_file(self,json_file):

        with open(json_file, 'r') as f:
            data = json.load(f)
            # Extract relevant text data
            title = data.get('Title', '')
            authors = ', '.join(data.get('Authors', []))
            abstract = data.get('Abstract', '')
            keywords = ', '.join(data.get('Key Words', []))
            pubdate = data.get('Pub Date', '')
            # Concatenate text data
            text = f"{abstract} "
            meta = f"Title: {title} | Authors: {authors} | Keywords: {keywords} | Pubdate:{pubdate}"

            # Split the string by '|' to separate key-value pairs
            pairs = [pair.strip() for pair in meta.split('|')]
            # Create a dictionary by splitting each pair by ':' and stripping whitespaces
            meta_dict = {pair.split(':')[0].strip(): pair.split(':')[1].strip() for pair in pairs}

            # Split the text into documents
            docs = self.text_splitter.split_text(text)

            #update to the vector store
            self.update_vectorstore(docs, meta_dict)
