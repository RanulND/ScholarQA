// what are the current needs of LLM?
match (n {name:"LLM"})-[r:NEED]->(c)
return c.name AS name, r.sentence AS Relationship

// What need to be improved in LLMs?
match (n {name:"LLM"})-[r:NEED|IMPROVES]->(c)
return c.name AS name, r.sentence AS Relationship

// What are the capabilities of LLMs?
match (n {name: "large language model"})-[r]->(c:Capability)
return c.name AS capability

// Full-text Index Search
CALL db.index.fulltext.queryRelationships("llmRelations", "LLMs") YIELD relationship, score
RETURN type(relationship), relationship.sentence, score