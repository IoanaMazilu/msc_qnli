rent_cost_premise = 160
rent_cost_hypothesis = 360

# the hypothesis refers to the cost of renting the tool mentioned in the premise
if rent_cost_premise >= rent_cost_hypothesis:
    # check if the cost in the premise contradicts the cost in the hypothesis
    label = "contradiction"
else:
    # if the cost in the premise does not contradict the cost in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
