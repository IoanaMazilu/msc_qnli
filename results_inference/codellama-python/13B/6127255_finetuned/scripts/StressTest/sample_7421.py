floor_premise = 11
floor_hypothesis = 81
rate_premise = 57
rate_hypothesis = 57

# the hypothesis refers to the floor number and rate of the elevator ride mentioned in the premise
if floor_hypothesis!= floor_premise:
    # check if the floor number in the hypothesis contradicts the floor number reported in the premise
    label = "contradiction"
elif rate_hypothesis!= rate_premise:
    # check if the rate of the elevator ride in the hypothesis contradicts the rate of the elevator ride reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
