floor_premise = 11
floor_hypothesis = 71
rate_premise = 87
rate_hypothesis = 87

# the hypothesis refers to the floor Steve gets on and the rate he rides up, both mentioned in the premise
if floor_premise!= floor_hypothesis:
    # check if the floor number in the hypothesis contradicts the floor number in the premise
    label = "contradiction"
elif rate_premise!= rate_hypothesis:
    # check if the rate in the hypothesis contradicts the rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
