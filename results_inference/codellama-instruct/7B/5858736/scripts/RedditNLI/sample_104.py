import re

# extract numerical entities from the premise and hypothesis
premise_entities = re.findall(r"\d+", premise)
hypothesis_entities = re.findall(r"\d+", hypothesis)

# convert numerical entities to integers
premise_entities = [int(entity) for entity in premise_entities]
hypothesis_entities = [int(entity) for entity in hypothesis_entities]

# define variables for the comparison
richest_people = premise_entities[0]
population = premise_entities[1]

# define variables for the comparison
richest_people_hypothesis = hypothesis_entities[0]
population_hypothesis = hypothesis_entities[1]

# compare the variables
if richest_people_hypothesis!= richest_people:
    # check if the number of richest people in the hypothesis contradicts the number of richest people in the premise
    label = "contradiction"
elif population_hypothesis!= population:
    # check if the number of people in the hypothesis contradicts the number of people in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
