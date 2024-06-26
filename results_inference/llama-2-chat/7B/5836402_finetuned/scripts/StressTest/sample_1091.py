matthew_walking_rate_premise = 3
matthew_walking_rate_hypothesis = 3
johnny_walking_rate_premise = 4
johnny_walking_rate_hypothesis = 4

# the hypothesis refers to the walking rates of Matthew and Johnny mentioned in the premise
if matthew_walking_rate_premise <= matthew_walking_rate_hypothesis:
    # check if the estimate of'matthew_walking_rate_hypothesis' contradicts the walking rate of Matthew in the premise
    label = "contradiction"
elif johnny_walking_rate_hypothesis!= johnny_walking_rate_premise:
    # check if the walking rate of Johnny in the hypothesis contradicts the walking rate of Johnny reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)