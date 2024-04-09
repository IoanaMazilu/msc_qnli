production_increase_premise = 1.5
production_increase_hypothesis = 1.5

# the hypothesis and premise mention the production increase needed to match oil demand and supply in the second half of the year
if production_increase_hypothesis!= production_increase_premise:
    # check if the production increase in the hypothesis contradicts the production increase in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
