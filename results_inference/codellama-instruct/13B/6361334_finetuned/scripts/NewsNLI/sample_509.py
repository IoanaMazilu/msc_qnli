# define variables for the entities in the premise and hypothesis
premise_entities = ["experts", "two explosive devices", "trees", "area"]
hypothesis_entities = ["two explosive devices", "trees", "area"]

# check if the hypothesis mentions all the entities in the premise
if set(premise_entities).issubset(hypothesis_entities):
    # if the hypothesis mentions all the entities in the premise, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis does not mention all the entities in the premise, we can infer neutrality
    label = "neutral"

print(label)
