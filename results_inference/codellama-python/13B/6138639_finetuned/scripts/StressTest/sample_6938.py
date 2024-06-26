floor_premise = 11
floor_hypothesis = 11
rate_premise = 57
rate_hypothesis = 57

# the hypothesis refers to the floor Stalin gets on and the rate at which he rides up, both mentioned in the premise
if floor_hypothesis <= floor_premise:
    # check if the hypothesis value contradicts the floor mentioned in the premise
    label = "contradiction"
elif rate_hypothesis!= rate_premise:
    # check if the rate mentioned in the hypothesis contradicts the rate mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
