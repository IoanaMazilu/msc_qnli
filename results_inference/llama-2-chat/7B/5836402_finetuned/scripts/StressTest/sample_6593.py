floor_start_premise = 71
floor_start_hypothesis = 31
elevator_speed_premise = 93
elevator_speed_hypothesis = 93

# the hypothesis refers to the floor number and the speed of the elevator mentioned in the premise
if floor_start_hypothesis!= floor_start_premise:
    # check if the floor number in the hypothesis contradicts the floor number in the premise
    label = "contradiction"
elif elevator_speed_hypothesis!= elevator_speed_premise:
    # check if the elevator speed in the hypothesis contradicts the elevator speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
