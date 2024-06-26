elevator_floor_premise = 61
elevator_floor_hypothesis = 51
elevator_rate_premise = 63
elevator_rate_hypothesis = 63

# the hypothesis refers to the floor and rate of the elevator, both mentioned in the premise
if elevator_floor_hypothesis >= elevator_floor_premise:
    # check if the hypothesis value contradicts the estimate of less than 'elevator_floor_premise'
    label = "contradiction"
elif elevator_rate_hypothesis!= elevator_rate_premise:
    # check if the rate of the elevator in the hypothesis contradicts the rate of the elevator reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
