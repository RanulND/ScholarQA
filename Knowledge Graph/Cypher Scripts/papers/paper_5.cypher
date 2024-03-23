create (p5:Paper { 
    title:"Can Large Language Models Provide Feedback to Students? A Case Study on ChatGPT", 
    publishedDate:Date("2023-07-13"), 
    doi: "10.1109/ICALT58122.2023.00100", 
    abstract:"educational feedback has been widely acknowledged as an effective approach to improving student learning. however, scaling effective practices can be laborious and costly, which motivated researchers to work on automated feedback systems (afs). inspired by the recent advancements in the pre-trained language models (e.g., chatgpt), we posit that such models might advance the existing knowledge of textual feedback generation in afs because of their capability to offer natural-sounding and detailed responses. therefore, we aimed to investigate the feasibility of using chatgpt to provide students with feedback to help them learn better. our results show that i) chatgpt is capable of generating more detailed feedback that fluently and coherently summarizes students' performance than human instructors; ii) chatgpt achieved high agreement with the instructor when assessing the topic of students' assignments; and iii) chatgpt could provide feedback on the process of students completing the task, which might benefit students developing learning skills"
    })
 
merge (wei:Author {name:"wei dai"})
merge (jionghao:Author {name:"jionghao lin"})
merge (hua:Author {name:"hua jin"})
merge (tongguang:Author {name:"tongguang li"})
merge (yi:Author {name:"yi-shan tsai"})
merge (dragan:Author {name:"dragan ga\u0161evi\u0107"})
merge (guanliang:Author {name:"guanliang chen"})

merge (llm:Technology {name:"large language model"})
merge (afs:Technology {name:"automatic feedback system"})
merge (ef:Technology {name:"educational feedback"})
merge (chatbot:Technology {name:"chatbot"})
merge (chatgpt:Example {name:"chatgpt"})
merge (naturalSounding:Capability {name:"offer natural-sounding and detailed responses"})
merge (highAgreement:Capability {name:"achieved high agreement with the instructor when assessing the topic of students' assignments"})
merge (detailedFeedback:Capability {name:"generating more detailed feedback that fluently and coherently summarizes students' performance than human instructors"})
merge (provideFeedback:Capability {name:"provide feedback on the process of students completing the task"})
merge (studentLearning:Application {name:"student learning"})
merge (chatgptResult:Result {name:"i) ChatGPT is capable of generating more detailed feedback that fluently and coherently summarizes students' performance than human instructors; ii) ChatGPT achieved high agreement with the instructor when assessing the topic of students' assignments; and iii) ChatGPT could provide feedback on the process of students completing the task"})


create
    (wei)-[:AUTHORED]->(p5),
    (jionghao)-[:AUTHORED]->(p5),
    (hua)-[:AUTHORED]->(p5),
    (tongguang)-[:AUTHORED]->(p5),
    (yi)-[:AUTHORED]->(p5),
    (dragan)-[:AUTHORED]->(p5),
    (guanliang)-[:AUTHORED]->(p5)

create
    (p5)-[:DISCUSS]->(chatbot),
    (p5)-[:DISCUSS]->(ef),
    (p5)-[:DISCUSS]->(afs),
    (p5)-[:DELIVER]->(chatgptResult),
    (afs)-[:UTILIZE]->(llm),
    (chatgpt)-[:IS]->(llm),
    (chatgpt)-[:CAN]->(naturalSounding),
    (chatgpt)-[:CAN]->(highAgreement),
    (chatgpt)-[:CAN]->(detailedFeedback),
    (chatgpt)-[:CAN]->(provideFeedback),
    (studentLearning)-[:NEED]->(ef)
