import re

# extract numerical entities from the premise and hypothesis
premise_entities = re.findall(r"\d+", premise)
hypothesis_entities = re.findall(r"\d+", hypothesis)

# convert numerical entities to integers
premise_entities = [int(entity) for entity in premise_entities]
hypothesis_entities = [int(entity) for entity in hypothesis_entities]

# compare the numerical entities in the premise and hypothesis
if premise_entities[0]!= hypothesis_entities[0]:
    # check if the number of years in the hypothesis contradicts the number of years in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
