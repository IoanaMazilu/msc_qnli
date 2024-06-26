floor_premise = 11
floor_hypothesis = 81
rate_premise = 57
rate_hypothesis = 57

# the hypothesis refers to the floor number and rate of David's elevator ride mentioned in the premise
if floor_premise!= floor_hypothesis:
    # check if the floor number in the hypothesis contradicts the floor number in the premise
    label = "contradiction"
elif rate_premise!= rate_hypothesis:
    # check if the rate of ride in the hypothesis contradicts the rate of ride in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
