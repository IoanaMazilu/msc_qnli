start_floor_premise = 11
start_floor_hypothesis = 71
rate_premise = 87
rate_hypothesis = 87

# the hypothesis refers to the floor number and rate of the elevator ride mentioned in the premise
if start_floor_premise!= start_floor_hypothesis:
    # check if the floor number in the hypothesis contradicts the floor number reported in the premise
    label = "contradiction"
elif rate_premise!= rate_hypothesis:
    # check if the rate of the elevator ride in the hypothesis contradicts the rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
