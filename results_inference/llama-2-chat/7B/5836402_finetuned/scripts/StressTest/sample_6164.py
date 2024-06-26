wheat_kg_premise = 30
wheat_kg_hypothesis = 30

# the hypothesis refers to the weight of wheat purchased, which is also mentioned in the premise
if wheat_kg_hypothesis <= wheat_kg_premise:
    # check if the hypothesis value contradicts the estimate of 'wheat_kg_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
