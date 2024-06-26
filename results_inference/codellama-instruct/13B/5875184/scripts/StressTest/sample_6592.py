elevator_floor_premise = 51
elevator_floor_hypothesis = 71
elevator_speed_premise = 93
elevator_speed_hypothesis = 93

# the hypothesis refers to the specific floor and speed mentioned in the premise
if elevator_floor_hypothesis <= elevator_floor_premise:
    # check if the hypothesis value contradicts the estimate of more than 'elevator_floor_premise'
    label = "contradiction"
elif elevator_speed_hypothesis!= elevator_speed_premise:
    # check if the speed in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
