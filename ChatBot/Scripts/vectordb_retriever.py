# import required libraries
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings.sentence_transformer import SentenceTransformerEmbeddings


class vector_retriever:
    """

    This class is to do a vector search in the FAISS vectore db.

    """

    def __init__(self):

        """
        initializing the class to call the vector db for answer retreival.

        output:
            vecotr db
        """

        self.model = 'Models/embedding-allenai-specter'
        self.db = 'DataBase/VectorDB/vectorstore'


    # Function for loading the embedding model
    def load_embedding_model(self, normalize_embedding=True):
        return SentenceTransformerEmbeddings(
            model_name=  self.model ,
            model_kwargs={'device':'cpu'}, # here we will run the model with CPU only
            encode_kwargs = {
                'normalize_embeddings': normalize_embedding # keep True to compute cosine similarity
            }
        )
    
    # Function to load the vecotr db
    def load_db(self):
        embeddings = self.load_embedding_model() #load sentence transformer
        db = FAISS.load_local(folder_path=self.db,
                      embeddings=embeddings,
                      allow_dangerous_deserialization=True)
        return db

