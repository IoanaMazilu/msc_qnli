floor_premise = 71
floor_hypothesis = 31
rate_premise = 93
rate_hypothesis = 93

# the hypothesis talks about the floor and rate of the elevator, both mentioned in the premise
if floor_premise!= floor_hypothesis:
    # check if the floor in the hypothesis contradicts the floor in the premise
    label = "contradiction"
elif rate_premise!= rate_hypothesis:
    # check if the rate in the hypothesis contradicts the rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
