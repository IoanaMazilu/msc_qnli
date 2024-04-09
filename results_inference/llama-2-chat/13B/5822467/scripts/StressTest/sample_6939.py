elevator_floor_premise = 51
elevator_floor_hypothesis = 61
rate_per_minute_premise = 63

# the hypothesis refers to the floor where Jose gets on the elevator and the rate at which the elevator descends
if elevator_floor_hypothesis <= elevator_floor_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif rate_per_minute_premise!= rate_per_minute_hypothesis:
    # check if the rate at which the elevator descends in the hypothesis contradicts the rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
