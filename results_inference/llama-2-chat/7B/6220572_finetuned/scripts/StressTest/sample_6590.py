elevator_floor_premise = 11
elevator_floor_hypothesis = 71
elevator_speed_premise = 87
elevator_speed_hypothesis = 87

# the hypothesis talks about the floor and speed of the elevator, referenced also in the premise
if elevator_floor_hypothesis!= elevator_floor_premise:
    # check if the floor number in the hypothesis contradicts the floor number in the premise
    label = "contradiction"
elif elevator_speed_hypothesis!= elevator_speed_premise:
    # check if the speed of the elevator in the hypothesis contradicts the speed of the elevator reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
