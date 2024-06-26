import re

# Extract numerical entities from the premise and hypothesis
premise_num_entities = re.findall(r'\d+', premise)
hypothesis_num_entities = re.findall(r'\d+', hypothesis)

# Convert numerical entities to integers
premise_num_entities = [int(num_entity) for num_entity in premise_num_entities]
hypothesis_num_entities = [int(num_entity) for num_entity in hypothesis_num_entities]

# Check if the number of entities in the hypothesis contradicts the number of entities in the premise
if len(hypothesis_num_entities)!= len(premise_num_entities):
    label = "contradiction"
else:
    # Check if the entities in the hypothesis are consistent with the premise
    if all(entity_hypothesis >= entity_premise for entity_hypothesis, entity_premise in zip(hypothesis_num_entities, premise_num_entities)):
        label = "entailment"
    else:
        label = "neutral"

print(label)
