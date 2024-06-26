elevator_floor_premise = 11
elevator_floor_hypothesis = 71
elevator_rate_premise = 87
elevator_rate_hypothesis = 87

# the hypothesis refers to the floor number and rate of the elevator ride, both mentioned in the premise
if elevator_floor_hypothesis <= elevator_floor_premise:
    # check if the estimate of 'elevator_floor_hypothesis' contradicts the number of the floor in the premise
    label = "contradiction"
elif elevator_rate_hypothesis!= elevator_rate_premise:
    # check if the rate of the elevator ride in the hypothesis contradicts the rate mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
