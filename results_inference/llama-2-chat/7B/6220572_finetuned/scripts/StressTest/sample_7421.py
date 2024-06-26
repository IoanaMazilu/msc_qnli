start_floor_premise = 11
start_floor_hypothesis = 81
ride_rate_premise = 57
ride_rate_hypothesis = 57

if start_floor_hypothesis <= start_floor_premise:
    # check if the starting floor of the hypothesis contradicts the starting floor in the premise
    label = "contradiction"
elif ride_rate_hypothesis!= ride_rate_premise:
    # check if the ride rate in the hypothesis contradicts the ride rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)
