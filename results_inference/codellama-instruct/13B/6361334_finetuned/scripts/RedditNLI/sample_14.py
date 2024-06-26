demand_premise = 1.5
demand_hypothesis = 1.5

# the hypothesis and premise mention the amount of oil demand that needs to be increased to avoid a shortfall
if demand_premise!= demand_hypothesis:
    # check if the demand in the hypothesis contradicts the demand in the premise
    label = "contradiction"
else:
    # if the demand in the hypothesis is the same as the demand in the premise, we can infer entailment
    label = "entailment"

print(label)
