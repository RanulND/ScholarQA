create (p2:Paper { 
    title:"Prompting Large Language Models with Answer Heuristics for Knowledge-Based Visual Question Answering", 
    publishedDate:Date("2023-06-17"), 
    doi: "10.1109/CVPR52729.2023.01438", 
    abstract:"knowledge-based visual question answering (vqa) requires external knowledge beyond the image to answer the question. early studies retrieve required knowledge from explicit knowledge bases (kbs), which often introduces irrelevant information to the question, hence restricting the performance of their models. recent works have sought to use a large language model (i.e., gpt-3 [3]) as an implicit knowledge engine to acquire the necessary knowledge for answering. despite the encouraging results achieved by these methods, we argue that they have not fully activated the capacity of gpt-3 as the provided input information is insufficient. in this paper, we present prophet-a conceptually simple framework designed to\u00a0prompt\u00a0gpt-3 with answer heuristics for knowledge-based vqa. specifically, we first train a vanilla vqa model on a specific knowledge-based vqa dataset without external knowledge. after that, we extract two types of complementary answer heuristics from the model: answer candidates and answer-aware examples. finally, the two types of answer heuristics are encoded into the prompts to enable gpt-3 to better comprehend the task thus enhancing its capacity. prophet significantly outperforms all existing state-of-the-art methods on two challenging knowledge-based vqa datasets, ok-vqa and a-okvqa, delivering 61.1% and 55.7% accuracies on their testing sets, respectively"
    })
 
merge (zhenwei:Author {name:"zhenwei shao"})
merge (zhou:Author {name:"zhou yu"})
merge (meng:Author {name:"meng wang"})
merge (jun:Author {name:"jun yu"})

merge (kbvqa:Technology {name:"knowledge based visual question answering"})
merge (vqa:Technology {name:"visual question answering"})
merge (llm:Technology {name:"large language model"})
merge (gpt3:Example {name:"gpt-3"})
merge (prophetA:Invention {name:"Prophet-a"})
merge (okvqa:Dataset {name:"ok-vqa"})
merge (aokvqa:Dataset {name:"a-okvqa"})
merge (knowledge:Requirement {name:"knowledge"})
merge (image:Requirement {name:"image"})
merge (irrInfo:Drawback {name:"introduces irrelevant information"})
merge (challenge:Result {name:"on two challenging knowledge-based VQA datasets, OK-VQA and A-OKVQA, delivering 61.1% and 55.7% accuracies on their testing sets, respectively"})
merge (sugestion:Method {name:"we first train a vanilla VQA model on a specific knowledge-based VQA dataset without external knowledge. After that, we extract two types of complementary answer heuristics from the model: answer candidates and answer-aware examples. Finally, the two types of answer heuristics are encoded into the prompts to enable GPT-3 to better comprehend the task thus enhancing its capacity"})
merge (promptAnswer:Capability {name:"prompt GPT-3 with answer heuristics for knowledge-based via"})

create
    (zhenwei)-[:AUTHORED]->(p2),
    (zhou)-[:AUTHORED]->(p2),
    (meng)-[:AUTHORED]->(p2),
    (jun)-[:AUTHORED]->(p2)

create
    (p2)-[:DISCUSS]->(vqa),
    (p2)-[:DISCUSS]->(kbvqa),
    (p2)-[:DEVELOP]->(prophetA),
    (p2)-[:DELIVER]->(challenge),
    (p2)-[:SUGGEST]->(sugestion),
    (prophetA)-[:TO]->(promptAnswer),
    (vqa)-[:USE]->(okvqa),
    (vqa)-[:USE]->(aokvqa),
    (vqa)<-[:NEED]-(knowledge),
    (vqa)<-[:NEED]-(image),
    (prophetA)-[:OUTPERFORM]->(vqa),
    (vqa)-[:MAY]->(irrInfo),
    (vqa)<-[:UTILIZE]-(llm),
    (gpt3)-[:IS]->(llm)
