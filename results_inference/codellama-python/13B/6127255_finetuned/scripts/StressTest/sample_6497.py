bus_speed_premise = 50
bus_speed_hypothesis = 50
bus_time_premise = 44
bus_time_hypothesis = 14

# the hypothesis refers to the speed and time of the bus journey mentioned in the premise
if bus_speed_hypothesis!= bus_speed_premise:
    # check if the speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
elif bus_time_hypothesis > bus_time_premise:
    # check if the time in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
