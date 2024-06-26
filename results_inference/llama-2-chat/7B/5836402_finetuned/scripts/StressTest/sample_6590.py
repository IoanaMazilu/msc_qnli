floor_premise = 11
floor_hypothesis = 71
elevator_speed_premise = 87
elevator_speed_hypothesis = 87

# the hypothesis refers to the floor and elevator speed mentioned in the premise
if floor_hypothesis!= floor_premise:
    # check if the floor in the hypothesis contradicts the floor mentioned in the premise
    label = "contradiction"
elif elevator_speed_hypothesis!= elevator_speed_premise:
    # check if the elevator speed in the hypothesis contradicts the elevator speed mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
