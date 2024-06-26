floor_premise = 51
floor_hypothesis = 31
rate_premise = 63
rate_hypothesis = 63

# the hypothesis refers to the floor and rate of the elevator ride mentioned in the premise
if floor_hypothesis!= floor_premise:
    # check if the floor number in the hypothesis contradicts the floor number reported in the premise
    label = "contradiction"
elif rate_hypothesis!= rate_premise:
    # check if the rate of floors per minute in the hypothesis contradicts the rate of floors per minute reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
