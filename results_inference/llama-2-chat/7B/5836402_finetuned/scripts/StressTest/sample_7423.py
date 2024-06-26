elevator_floor_premise = 61
elevator_floor_hypothesis = 51
elevator_speed_premise = 63
elevator_speed_hypothesis = 63

# the hypothesis refers to the floor of the elevator and its speed, which are also mentioned in the premise
if elevator_floor_premise <= elevator_floor_hypothesis:
    # check if the estimate of 'elevator_floor_hypothesis' contradicts the floor of the elevator in the premise
    label = "contradiction"
elif elevator_speed_hypothesis!= elevator_speed_premise:
    # check if the speed of the elevator in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
