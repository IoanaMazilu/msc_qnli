rent_cost_premise = 160
rent_cost_hypothesis = 760

# the hypothesis refers to the cost of renting a tool mentioned in the premise
if rent_cost_premise!= rent_cost_hypothesis:
    # check if the cost of renting a tool in the hypothesis contradicts the cost of renting a tool in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
