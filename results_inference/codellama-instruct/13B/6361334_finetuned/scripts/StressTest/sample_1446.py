premise_deaths = 0.05
hypothesis_deaths = 0.04
premise_fleeing = 0.15
hypothesis_fleeing = 0.15

# the hypothesis refers to the number of deaths and fleeing people mentioned in the premise
if hypothesis_deaths <= premise_deaths:
    # check if the estimate of 'hypothesis_deaths' contradicts the number of deaths in the premise
    label = "contradiction"
elif hypothesis_fleeing!= premise_fleeing:
    # check if the number of fleeing people in the hypothesis contradicts the number of fleeing people reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
