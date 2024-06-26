wheat_kg_premise = 30
wheat_kg_hypothesis = 10

# the hypothesis refers to the amount of wheat purchased by Arun, which is also mentioned in the premise
if wheat_kg_hypothesis >= wheat_kg_premise:
    # check if the estimate of 'wheat_kg_hypothesis' contradicts the amount of wheat purchased in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
