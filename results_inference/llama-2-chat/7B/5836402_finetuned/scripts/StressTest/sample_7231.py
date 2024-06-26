wheat_kg_premise = 40
wheat_kg_hypothesis = 30

# the hypothesis refers to the quantity of wheat purchased by Arun mentioned in the premise
if wheat_kg_hypothesis >= wheat_kg_premise:
    # check if the estimate of 'wheat_kg_hypothesis' contradicts the quantity of wheat purchased in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
