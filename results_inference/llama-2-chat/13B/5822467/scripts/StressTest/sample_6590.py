floor_premise = 11
rate_premise = 87
floor_hypothesis = 71
rate_hypothesis = 87

# the hypothesis refers to the floor where Steve gets on the elevator and the rate at which he rides up
if floor_hypothesis <= floor_premise:
    # check if the estimate of 'floor_hypothesis' contradicts the floor mentioned in the premise
    label = "contradiction"
elif rate_hypothesis!= rate_premise:
    # check if the rate at which Steve rides up in the hypothesis contradicts the rate mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
