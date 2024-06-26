start_floor_premise = 11
start_floor_hypothesis = 71
elevator_speed_premise = 87
elevator_speed_hypothesis = 87

# the hypothesis refers to the floor where Steve gets on the elevator and the elevator speed, both also mentioned in the premise
if start_floor_premise != start_floor_hypothesis:
    # check if the start floor in the hypothesis contradicts the start floor in the premise
    label = "contradiction"
elif elevator_speed_hypothesis != elevator_speed_premise:
    # check if the elevator speed in the hypothesis contradicts the elevator speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
