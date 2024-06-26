people_dead_premise = 0.10
people_dead_hypothesis = 0.10
people_left_premise = 0.20
people_left_hypothesis = 0.20

# the hypothesis refers to the percentage of people who died and left the village
if people_dead_hypothesis <= people_dead_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif people_left_hypothesis!= people_left_premise:
    # check if the percentage of people who left the village in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
