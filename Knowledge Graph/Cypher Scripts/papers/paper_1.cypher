create (p1:Paper { 
    title:"ProgPrompt: Generating Situated Robot Task Plans using Large Language Models", 
    publishedDate:Date("2023-05-29"), 
    doi: "10.1109/ICRA48891.2023.10161317", 
    abstract:"Task planning can require defining myriad domain knowledge about the world in which a robot needs to act. To ameliorate that effort, large language models (LLMs) can be used to score potential next actions during task planning, and even generate action sequences directly, given an instruction in natural language with no additional domain information. However, such methods either require enumerating all possible next steps for scoring, or generate free-form text that may contain actions not possible on a given robot in its current context. We present a programmatic LLM prompt structure that enables plan generation functional across situated environments, robot capabilities, and tasks. Our key insight is to prompt the LLM with program-like specifications of the available actions and objects in an environment, as well as with example programs that can be executed. We make concrete recommendations about prompt structure and generation constraints through ablation experiments, demonstrate state of the art success rates in VirtualHome household tasks, and deploy our method on a physical robot arm for tabletop tasks"
    })
 
merge (ishika:Author {name:"ishika singh"})
merge (valts:Author {name:"valts blukis"})
merge (arsalan:Author {name:"arsalan mousavian"})
merge (ankit:Author {name:"ankit goyal"})
merge (daniel:Author {name:"danfei xu"})
merge (jonathan:Author {name:"jonathan tremblay"})
merge (dieter:Author {name:"dieter fox"})
merge (jesse:Author {name:"jesse thomason"})
merge (animesh:Author {name:"animesh garg"})


merge (keyInsight:Method {name:"Our key insight is to prompt the LLM with program-like specifications of the available actions and objects in an environment, as well as with example programs that can be executed."})
merge (taskPlanning:Technology {name:"task planning"})
merge (promptStructure:Domain {name:" prompt structure for task planning"})
merge (llm:Technology {name:"large language model"})
merge (actionSequence:Capability {name:"generate action sequences"})
merge (nextActions:Capability {name:"score next actions"})
merge (robotArm:Application {name:"robot arm"})
merge (vhht:Application {name:"virtual home household task"})

create
    (ishika)-[:AUTHORED]->(p1),
    (valts)-[:AUTHORED]->(p1),
    (arsalan)-[:AUTHORED]->(p1),
    (ankit)-[:AUTHORED]->(p1),
    (daniel)-[:AUTHORED]->(p1),
    (jonathan)-[:AUTHORED]->(p1),
    (dieter)-[:AUTHORED]->(p1),
    (jesse)-[:AUTHORED]->(p1),
    (animesh)-[:AUTHORED]->(p1)


create
    (taskPlanning)<-[:NEED]-(vhht),
    (taskPlanning)<-[:NEED]-(robotArm),
    (p1)-[:SUGGEST]->(keyInsight),
    (p1)-[:DISCUSS]->(promptStructure),
    (p1)-[:DISCUSS]->(taskPlanning),
    (promptStructure)-[:UTILIZE]->(llm),
    (taskPlanning)-[:UTILIZE]->(llm),
    (llm)-[:TO]->(actionSequence),
    (llm)-[:TO]->(nextActions)


