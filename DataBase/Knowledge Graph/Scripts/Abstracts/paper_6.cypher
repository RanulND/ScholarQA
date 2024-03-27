create (p6:Paper { 
    title:"Jigsaw: Large Language Models meet Program Synthesis", 
    publishedDate:Date("2022-05-27"), 
    doi: "10.1145/3510003.3510203", 
    abstract:"large pre-trained language models such as gpt-3 [10], codex [11], and coogle's language model [7] are now capable of generating code from natural language specifications of programmer intent. we view these developments with a mixture of optimism and caution. on the optimistic side, such large language models have the potential to improve productivity by providing an automated ai pair programmer for every programmer in the world. on the cautionary side, since these large language models do not understand program semantics, they offer no guarantees about quality of the suggested code. in this paper, we present an approach to augment these large language models with post-processing steps based on program analysis and synthesis techniques, that understand the syntax and semantics of programs. further, we show that such techniques can make use of user feedback and improve with usage. we present our experiences from building and evaluating such a tool jigsaw, targeted at synthesizing code for using python pandas api using multi-modal inputs. our experience suggests that as these large language models evolve for synthesizing code from intent, jigsaw has an important role to play in improving the accuracy of the systems"
    })
 
merge (naman:Author {name:"naman jain"})
merge (skanda:Author {name:"skanda vaidyanath"})
merge (arun:Author {name:"arun iyer"})
merge (nagarajan:Author {name:"nagarajan natarajan"})
merge (suresh:Author {name:"suresh parthasarathy"})
merge (sriram:Author {name:"sriram rajamani"})
merge (rahul:Author {name:"rahul sharma"})

merge (llm:Technology {name:"large language model"})
merge (gpt3:Example {name:"gpt-3"})
merge (codex:Example {name:"codex"})
merge (clm:Example {name:"coogle language model"})
merge (m:Method {name:"we present an approach to augment these large language models with post-processing steps based on program analysis and synthesis techniques, that understand the syntax and semantics of programs. Further, we show that such techniques can make use of user feedback and improve with usage."})
merge (codeGeneration:Technology {name:"code generation"})
merge (generateCode:Capability {name:"generate code from natural language specifications of programmer intent"})
merge (d:Drawback {name:"offer no guarantees about quality of the suggested code"})
merge (r:Reason {name:"large language models do not understand program semantics"})
merge (jigsaw:Invention {name:"jigsaw"})
merge (synthesizeCode:Capability {name:"synthesizing code for using Python Pandas API using multi-modal inputs"})
merge (improveProductivity:Capability {name:"improve productivity by providing an automated AI pair programmer for every programmer in the world"})

create
    (naman)-[:AUTHORED]->(p6),
    (skanda)-[:AUTHORED]->(p6),
    (arun)-[:AUTHORED]->(p6),
    (nagarajan)-[:AUTHORED]->(p6),
    (suresh)-[:AUTHORED]->(p6),
    (sriram)-[:AUTHORED]->(p6),
    (rahul)-[:AUTHORED]->(p6)

create
    (p6)-[:DISCUSS]->(codeGeneration),
    (p6)-[:DISCUSS]->(llm),
    (p6)-[:SUGGEST]->(m),
    (p6)-[:DEVELOP]->(jigsaw),
    (gpt3)-[:IS]->(llm),
    (codex)-[:IS]->(llm),
    (clm)-[:IS]->(llm),
    (llm)-[:CAN]->(improveProductivity),
    (llm)-[:CAN]->(generateCode),
    (llm)-[:MAY]->(d),
    (d)-[:BECAUSE]->(r),
    (jigsaw)-[:TO]->(synthesizeCode)
