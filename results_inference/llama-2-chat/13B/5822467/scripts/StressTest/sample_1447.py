people_died_premise = 4
people_died_hypothesis = 5
remainder_left_premise = 15
remainder_left_hypothesis = 15

# the hypothesis refers to the percentage of people who died and the remainder who left the village
if people_died_hypothesis <= people_died_premise:
    # check if the estimate of 'people_died_hypothesis' contradicts the number of people who died in the premise
    label = "contradiction"
elif remainder_left_hypothesis!= remainder_left_premise:
    # check if the number of people who left the village in the hypothesis contradicts the number of people who left the village reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
