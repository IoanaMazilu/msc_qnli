distance_ran_premise = 8
distance_ran_hypothesis = 5

# the hypothesis refers to the distance ran by the sisters, which is also mentioned in the premise
if distance_ran_premise <= distance_ran_hypothesis:
    # check if the estimate of 'distance_ran_hypothesis' contradicts the number of km ran in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)