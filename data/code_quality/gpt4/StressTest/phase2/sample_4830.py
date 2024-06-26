matthew_rate_premise = 3
matthew_rate_hypothesis = 1
johnny_rate_premise = 4
johnny_rate_hypothesis = 4

# the hypothesis refers to the walking rates of Matthew and Johnny mentioned in the premise
if matthew_rate_premise <= matthew_rate_hypothesis:
    # check if the estimate of 'matthew_rate_hypothesis' contradicts the walking rate of Matthew in the premise
    label = "contradiction"
elif johnny_rate_premise != johnny_rate_hypothesis:
    # check if the walking rate of Johnny in the hypothesis contradicts the walking rate of Johnny reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
