distance_ran_premise = 2
distance_ran_hypothesis = 3

# the hypothesis talks about the distance ran by the sisters, which is also mentioned in the premise
if distance_ran_hypothesis <= distance_ran_premise:
    # check if the estimate of 'distance_ran_hypothesis' contradicts the distance in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
