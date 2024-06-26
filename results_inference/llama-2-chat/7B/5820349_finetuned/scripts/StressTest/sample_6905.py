rent_cost_premise = 160
rent_cost_hypothesis = 760

# the hypothesis refers to the cost of renting the tool mentioned in the premise
if rent_cost_premise!= rent_cost_hypothesis:
    # check if the cost in the hypothesis contradicts the cost reported in the premise
    label = "contradiction"
else:
    # if the cost in the hypothesis does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
