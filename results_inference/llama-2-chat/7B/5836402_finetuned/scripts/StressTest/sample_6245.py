people_premise = 120
people_hypothesis = 120
preference_premise = 0.6
preference_hypothesis = 0.6

# the hypothesis refers to the number of people and the preference rate mentioned in the premise
if people_hypothesis >= people_premise:
    # check if the number of people in the hypothesis contradicts the number of people reported in the premise
    label = "contradiction"
elif preference_hypothesis!= preference_premise:
    # check if the preference rate in the hypothesis contradicts the preference rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
