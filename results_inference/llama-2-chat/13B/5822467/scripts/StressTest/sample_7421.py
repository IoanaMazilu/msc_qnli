floor_premise = 11
floor_hypothesis = 81
rate_premise = 57

# the hypothesis refers to the floor where David gets on the elevator and the rate at which he rides up
if floor_hypothesis <= floor_premise:
    # check if the hypothesis value contradicts the premise floor
    label = "contradiction"
elif floor_premise!= rate_premise:
    # check if the rate mentioned in the hypothesis contradicts the rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
