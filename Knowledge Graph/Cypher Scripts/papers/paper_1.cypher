CREATE CONSTRAINT IF NOT EXISTS FOR (p:Paper) REQUIRE (p.doi) IS UNIQUE;

Create (p1:Paper { title:"ProgPrompt: Generating Situated Robot Task Plans using Large Language Models", y })

// create (p:Paper {title: "RecallM: An Adaptable Memory Mechanism with Temporal Understanding for Large Language Models",doi: "10.48550/arXiv.2307.02738",authors: ["Brandon Kynoch","Hugo Latapie","Dwane van der Sluis"],year:2023})
// create (llm:Comp_Term {name:"LLM"})
// create (task:Gen_Term {name:"Task"})
// create (ltm:Comp_Term {name: "Long-Term memory"})
// create (recallm:Finding {name: "RecallM"})
// create (beliefUpdating:Gen_Term {name:"Belief updating"})
// create (temporalUnderstanding:Gen_Term {name: "Temporal Understanding"})
// create (qaTask:Gen_Term {name: "Question & Answering Tasks"})
// create (inContext:Gen_Term {name: "In-context Learning"})

// create
// (p)-[:DISCUSS]->(llm),
// (p)-[:DISCUSS]->(recallm),
// (llm)-[:HAVE_CAPABILITIES {sentence:["Large Language Models (LLMs) have made extraordinary progress in the field of Artificial Intelligence and have demonstrated remarkable capabilities across a large variety of tasks and domains"]}]->(task),
// (llm)-[:NEED {sentence:["we recognize the need to supplement LLMs with long-term memory to overcome the context window limitation and, more importantly, to create a foundation for sustained reasoning, cumulative learning and long-term user interaction"]}]->(ltm),
// (recallm)-[:PROVIDES {sentence:["in this paper, we propose RecallM, a novel architecture for providing LLMs with an adaptable and updatable long-term memory mechanism"]}]->(ltm),
// (recallm)-[:IMPROVES {sentence:["In this paper we propose RecallM, a novel architecture for providing LLMs with an adaptable and updatable long-term memory mechanism"]}]->(llm),
// (recallm)-[:EFFECTIVE_AT {sentence:["Unlike previous methods, the RecallM architecture is particularly effective at belief updating and maintaining a temporal understanding of the knowledge provided to it"]}]->(beliefUpdating),
// (recallm)-[:EFFECTIVE_AT {sentence:["Unlike previous methods, the RecallM architecture is particularly effective at belief updating and maintaining a temporal understanding of the knowledge provided to it."]}]->(temporalUnderstanding),
// (recallm)-[:SHOWS_PERFORMANCE_ON {sentence:["We also demonstrate that RecallM shows competitive performance on general question-answering and in-context learning tasks"]}]->(qaTask),
// (recallm)-[:SHOWS_PERFORMANCE_ON {sentence:["We also demonstrate that RecallM shows competitive performance on general question-answering and in-context learning tasks"]}]->(inContext)
