oil_production_increase_premise = 1.5
oil_production_increase_hypothesis = 1.5

# the hypothesis and premise mention the increase in oil production needed to avoid a supply shortage
if oil_production_increase_premise!= oil_production_increase_hypothesis:
    # check if the increase in oil production in the hypothesis contradicts the increase in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
