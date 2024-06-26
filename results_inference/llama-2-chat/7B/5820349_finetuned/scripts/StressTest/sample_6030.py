distance_traveled_premise = 1/2
distance_traveled_hypothesis = 8/2

# the hypothesis refers to the distance traveled by Maria mentioned in the premise
if distance_traveled_premise >= distance_traveled_hypothesis:
    # check if the estimate of 'distance_traveled_hypothesis' contradicts the distance traveled in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
