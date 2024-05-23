floor_premise = 11
floor_hypothesis = 61
rate_premise = 57
rate_hypothesis = 57

# the hypothesis refers to the floor David gets on and the rate of the elevator, both mentioned in the premise
if floor_premise >= floor_hypothesis:
    # check if the floor number in the hypothesis contradicts the floor number in the premise
    label = "contradiction"
elif rate_premise!= rate_hypothesis:
    # check if the rate of the elevator in the hypothesis contradicts the rate of the elevator in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)