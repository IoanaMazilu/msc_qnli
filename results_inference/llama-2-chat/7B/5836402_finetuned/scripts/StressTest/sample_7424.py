elevator_floor_premise = 51
elevator_floor_hypothesis = 81
elevator_speed_premise = 63
elevator_speed_hypothesis = 63

# the hypothesis refers to the elevator floor and speed mentioned in the premise
if elevator_floor_hypothesis!= elevator_floor_premise:
    # check if the elevator floor in the hypothesis contradicts the elevator floor in the premise
    label = "contradiction"
elif elevator_speed_hypothesis!= elevator_speed_premise:
    # check if the elevator speed in the hypothesis contradicts the elevator speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
