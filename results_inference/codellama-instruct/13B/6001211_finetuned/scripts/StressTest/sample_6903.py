rent_cost_premise = 160
rent_cost_hypothesis = 360

# the hypothesis refers to the cost of renting a tool mentioned in the premise
if rent_cost_hypothesis <= rent_cost_premise:
    # check if the estimate of'rent_cost_hypothesis' contradicts the cost of rent in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
