floor_premise = 51
floor_hypothesis = 31
rate_premise = 63
rate_hypothesis = 63

# the hypothesis refers to the floor and rate of Jose's elevator ride mentioned in the premise
if floor_premise!= floor_hypothesis:
    # check if the floor number in the hypothesis contradicts the floor number reported in the premise
    label = "contradiction"
elif rate_premise!= rate_hypothesis:
    # check if the rate of descent in the hypothesis contradicts the rate of descent reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
