floor_premise = 51
floor_hypothesis = 31
rate_premise = 63
rate_hypothesis = 63

# the hypothesis refers to the floor Jose gets on and the rate of the elevator, both mentioned in the premise
if floor_premise!= floor_hypothesis:
    # check if the floor Jose gets on in the hypothesis contradicts the floor mentioned in the premise
    label = "contradiction"
elif rate_premise!= rate_hypothesis:
    # check if the rate of the elevator in the hypothesis contradicts the rate mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
