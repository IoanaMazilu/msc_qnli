wheat_kg_premise = 30
wheat_kg_hypothesis = 30

# the hypothesis refers to the number of kg of wheat purchased, mentioned in the premise
if wheat_kg_hypothesis <= wheat_kg_premise:
    # check if the estimate of 'wheat_kg_hypothesis' contradicts the number of kg of wheat in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
