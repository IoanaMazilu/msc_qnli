increase_production_premise = 1.5
increase_production_hypothesis = 1.5

# the hypothesis and premise mention the increase in oil production needed to avoid a shortfall
if increase_production_hypothesis!= increase_production_premise:
    # check if the increase in production in the hypothesis contradicts the increase in production in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
