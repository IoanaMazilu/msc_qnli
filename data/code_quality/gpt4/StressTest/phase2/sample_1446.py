died_premise = 5
died_hypothesis = 4
left_premise = 15
left_hypothesis = 15

# the hypothesis refers to the percentage of people who died and left the village in Sri Lanka, mentioned in the premise
if died_premise <= died_hypothesis:
    # check if the estimate of 'died_hypothesis' contradicts the percentage of people who died in the premise
    label = "contradiction"
elif left_hypothesis != left_premise:
    # check if the percentage of people who left the village in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
