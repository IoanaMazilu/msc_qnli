start_floor_premise = 11
start_floor_hypothesis = 71
rate_premise = 87
rate_hypothesis = 87

# the hypothesis refers to the starting floor and the rate of elevator ride mentioned in the premise
if start_floor_hypothesis!= start_floor_premise:
    # check if the starting floor in the hypothesis contradicts the starting floor reported in the premise
    label = "contradiction"
elif rate_hypothesis!= rate_premise:
    # check if the rate of ride in the hypothesis contradicts the rate of ride reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
