premise_cost = 190
hypothesis_cost = 190

# the premise and hypothesis mention the expected increase in labor costs
if premise_cost!= hypothesis_cost:
    # check if the cost in the hypothesis contradicts the cost in the premise
    label = "contradiction"
else:
    # if the cost values do not contradict, we can infer entailment
    label = "entailment"

print(label)
