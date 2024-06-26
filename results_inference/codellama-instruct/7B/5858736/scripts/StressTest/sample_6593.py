elevator_floor_premise = 71
elevator_floor_hypothesis = 31
elevator_rate_premise = 93
elevator_rate_hypothesis = 93

# the hypothesis refers to the floor and rate of the elevator mentioned in the premise
if elevator_floor_hypothesis!= elevator_floor_premise:
    # check if the hypothesis value contradicts the floor reported in the premise
    label = "contradiction"
elif elevator_rate_hypothesis!= elevator_rate_premise:
    # check if the hypothesis value contradicts the rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
