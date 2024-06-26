vehicle_value_premise = 1000000
vehicle_value_hypothesis = 1000000

# the hypothesis mentions the worth of the stolen vehicles, which is also mentioned in the premise
if vehicle_value_hypothesis!= vehicle_value_premise:
    # check if the vehicle value in the hypothesis contradicts the vehicle value reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
