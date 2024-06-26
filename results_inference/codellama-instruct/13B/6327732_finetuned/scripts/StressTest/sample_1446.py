premise_percentage_deaths = 5
hypothesis_percentage_deaths = 4
premise_percentage_fleeing = 15
hypothesis_percentage_fleeing = 15

# the hypothesis refers to the number of people who died by bombardment and fled the village, both mentioned in the premise
if hypothesis_percentage_deaths <= premise_percentage_deaths:
    # check if the estimate of 'hypothesis_percentage_deaths' contradicts the number of deaths in the premise
    label = "contradiction"
elif hypothesis_percentage_fleeing!= premise_percentage_fleeing:
    # check if the number of people who fled the village in the hypothesis contradicts the number of people who fled the village reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
