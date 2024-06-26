floors_premise = 11
floors_hypothesis = 61
minutes_per_floor_premise = 57

# the hypothesis refers to the floor where David gets on the elevator and the rate at which he rides up
if floors_hypothesis < floors_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif minutes_per_floor_premise!= minutes_per_floor_hypothesis:
    # check if the rate at which David rides up in the hypothesis contradicts the rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
