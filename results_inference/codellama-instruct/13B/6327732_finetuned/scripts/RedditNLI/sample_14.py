demand_premise = 1.5
demand_hypothesis = 1.5

# the hypothesis and premise mention the amount of oil needed to be produced to meet demand
if demand_premise!= demand_hypothesis:
    # check if the amount of oil needed to be produced in the hypothesis contradicts the amount needed in the premise
    label = "contradiction"
else:
    # if the amount of oil needed in the hypothesis is the same as the premise, we can infer entailment
    label = "entailment"

print(label)
