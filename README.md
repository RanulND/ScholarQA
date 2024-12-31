
<div align="center">
  <h1>Comparing the Performance of LLMs in RAG-Based Question-Answering: A Case Study in Computer Science Literature</h1>

  This is the repo containing all the codes and datasets used for the paper titles "Comparing the Performance of LLMs in RAG-Based Question-Answering: A Case Study in Computer Science Literature" presented at the 5th International Conference on Artificial Intelligence in Education Technology. [access the full paper here](10.1007/978-981-97-9255-9_26)
  <br></br>  
</div>

This paper compares the perfromance of popular open-source LLMs such as `Mistral-7b-instruct`, `LLaMa2-7b-chat`, `Falcon-7b-instruct` and `Orca-mini-v3-7b`, and OpenAI’s trending `GPT-3.5` in RAG based question-answering.

## 🌟 Guide to the repo

1. ChatBot<br>
Contains the scripts used for developing the chatbot.
- `chatbot_utils.py`: Contains the parameters set for each LLM
- `hybrid_chat.py`: The script to be used with a hybrid approach which uses answer candidates from knowledge graphs and langchain LLMchain to generate the answer.
- `prompt.py`: Contains user defined prompts to match different secenarios/LLMs
- `vectort_chat,py`: This creates the chat infrastructure by calling the chat history and vecot db retrived documents to answer the questions.
- `vectordb_retriever.py`:  This is to do a vector search in the FAISS vector db when user inputs a question.

2. DataBase <br> <br>
  2.1 Knowledge Graph
  -   Contains the script used to transform cypher text into Neo4J Knowledge Graph representations.<br>
  -   In this stage of the research knowledge graphs are not implemented fully. So please consider this as a testing phase and prioritize the vector db.

  2.2 VectorDB
  
  - Contains the script used to embed document text into vectors and store them in the FAISS vector db.
  - Please note that all the documents are first represented using the JSON format before embedding.
 
3. Document Processing
- Includes some of the pre processing steps carried out on the documents.
- Also includes the script to convert text documents into JSON format.

4. Evaluation
- A script to calculate the cosine similarity between generated answer and the answer candidate.
- Used to mathematiccaly determine the accuracy of the chatbot in answer generation.

5. Sample Files
- Contains some of the documents and their JSON docs we used to test the chatbot functionality.
- Please note all our LLM propost are engineered to answer the questions from the domanis covered in the sample data: `LLMs`, `Quantum Computing`, `Edge Computing`

## 🛠 Run it

1. Clone the repository to your local machine

   ```sh
   git clone https://github.com/RanulND/ScholarQA.git
   ```

2. Once the cloning process is completed, navigate into the cloned directory.

   ```sh
   cd ScholarQA-master
   ```

3. Install requirements

   ```sh
   pip install -r requirements.txt
   ```

### 🪄 Customise to match your style & feel the magic!
