floor_start_premise = 51
floor_start_hypothesis = 61
rate_elevator_premise = 63
rate_elevator_hypothesis = 63

# the hypothesis refers to the floor Albert gets on and the elevator's rate, both mentioned in the premise
if floor_start_hypothesis >= floor_start_premise:
    # check if the hypothesis value contradicts the floor 'floor_start_premise'
    label = "contradiction"
elif rate_elevator_hypothesis!= rate_elevator_premise:
    # check if the elevator's rate in the hypothesis contradicts the rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
