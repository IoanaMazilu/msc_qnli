percentage_dead_premise = 6
percentage_dead_hypothesis = 5
percentage_left_premise = 15
percentage_left_hypothesis = 15

# the hypothesis refers to the percentages of people who died and left the village mentioned in the premise
if percentage_dead_premise <= percentage_dead_hypothesis:
    # check if the estimated percentage of 'percentage_dead_hypothesis' contradicts the percentage of dead people in the premise
    label = "contradiction"
elif percentage_left_hypothesis != percentage_left_premise:
    # check if the percentage of people who left the village in the hypothesis contradicts the percentage of people who left the village reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
