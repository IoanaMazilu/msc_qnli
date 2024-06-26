rent_cost_premise = 125
rent_cost_hypothesis = 725

# the hypothesis refers to the cost of renting a tool mentioned in the premise
if rent_cost_hypothesis != rent_cost_premise:
    # if the cost in the hypothesis contradicts the cost mentioned in the premise
    label = "contradiction"
else:
    # if the cost in the hypothesis matches the cost in the premise
    label = "entailment"

print(label)
