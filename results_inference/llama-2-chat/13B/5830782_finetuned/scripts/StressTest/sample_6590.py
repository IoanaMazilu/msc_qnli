starting_floor_premise = 11
starting_floor_hypothesis = 71
rate_premise = 87
rate_hypothesis = 87

# the hypothesis refers to the starting floor and the rate of the elevator ride mentioned in the premise
if starting_floor_premise!= starting_floor_hypothesis:
    # check if the starting floor in the hypothesis contradicts the starting floor reported in the premise
    label = "contradiction"
elif rate_premise!= rate_hypothesis:
    # check if the rate of the ride in the hypothesis contradicts the rate of the ride reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
