floor_premise = 51
floor_hypothesis = 71
rate_premise = 93
rate_hypothesis = 93

# the hypothesis talks about the floor and rate of the elevator ride, which are also mentioned in the premise
if floor_premise!= floor_hypothesis:
    # check if the floor number in the hypothesis contradicts the floor number in the premise
    label = "contradiction"
elif rate_premise!= rate_hypothesis:
    # check if the rate of the elevator ride in the hypothesis contradicts the rate of the elevator ride in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
