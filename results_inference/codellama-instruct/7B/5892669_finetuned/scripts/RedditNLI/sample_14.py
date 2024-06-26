increase_production_premise = 1.5
increase_production_hypothesis = 1.5

# the hypothesis and premise mention the amount of oil production increase needed to meet demand
if increase_production_hypothesis!= increase_production_premise:
    # check if the amount of production increase in the hypothesis contradicts the amount of production increase in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
