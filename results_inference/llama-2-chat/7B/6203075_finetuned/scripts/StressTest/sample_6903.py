rent_cost_premise = 160
rent_cost_hypothesis = 360

# the hypothesis refers to the cost of renting the tool, which is also mentioned in the premise
if rent_cost_hypothesis <= rent_cost_premise:
    # check if the cost of renting in the hypothesis contradicts the cost of renting in the premise
    label = "contradiction"
else:
    # if the cost of renting in the hypothesis does not contradict the cost of renting in the premise, we can infer entailment
    label = "entailment"

print(label)
