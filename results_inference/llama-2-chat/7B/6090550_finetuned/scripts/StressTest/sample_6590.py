floor_premise = 11
floor_hypothesis = 71
rate_premise = 87
rate_hypothesis = 87

# the hypothesis refers to the floor and the rate of elevator travel mentioned in the premise
if floor_hypothesis!= floor_premise:
    # check if the floor in the hypothesis contradicts the floor mentioned in the premise
    label = "contradiction"
elif rate_hypothesis!= rate_premise:
    # check if the rate of elevator travel in the hypothesis contradicts the rate mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
