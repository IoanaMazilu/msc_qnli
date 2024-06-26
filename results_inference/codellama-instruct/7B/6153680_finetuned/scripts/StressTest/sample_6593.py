elevator_floor_premise = 71
elevator_floor_hypothesis = 31
elevator_rate_premise = 93
elevator_rate_hypothesis = 93

# the hypothesis refers to the same elevator ride as the premise, but with different floor numbers
if elevator_floor_premise!= elevator_floor_hypothesis:
    # check if the floor number in the hypothesis contradicts the floor number in the premise
    label = "contradiction"
elif elevator_rate_premise!= elevator_rate_hypothesis:
    # check if the rate of the elevator in the hypothesis contradicts the rate of the elevator in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
