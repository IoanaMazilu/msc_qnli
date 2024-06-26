percentage_deaths_premise = 5
percentage_deaths_hypothesis = 5
percentage_fleeing_premise = 15
percentage_fleeing_hypothesis = 15

# the hypothesis refers to the percentage of deaths and fleeing mentioned in the premise
if percentage_deaths_hypothesis <= percentage_deaths_premise:
    # check if the estimate of 'percentage_deaths_hypothesis' contradicts the percentage of deaths in the premise
    label = "contradiction"
elif percentage_fleeing_hypothesis!= percentage_fleeing_premise:
    # check if the percentage of fleeing in the hypothesis contradicts the percentage of fleeing reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
