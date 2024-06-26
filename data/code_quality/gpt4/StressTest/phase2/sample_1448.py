dead_percentage_premise = 5
dead_percentage_hypothesis = 7
left_percentage_premise = 15
left_percentage_hypothesis = 15

# the hypothesis refers to the percentage of people who died and left the village mentioned in the premise
if dead_percentage_hypothesis != dead_percentage_premise:
    # check if the percentage of people who died in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
elif left_percentage_hypothesis != left_percentage_premise:
    # check if the percentage of people who left the village in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
