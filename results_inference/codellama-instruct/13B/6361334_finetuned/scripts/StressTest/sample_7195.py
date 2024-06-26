distance_premise = 6
distance_hypothesis = 7

# the hypothesis refers to the time required to cover the distance between Chennai and Jammu, mentioned in the premise
if distance_premise <= distance_hypothesis:
    # check if the estimate of 'distance_hypothesis' contradicts the time required in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
