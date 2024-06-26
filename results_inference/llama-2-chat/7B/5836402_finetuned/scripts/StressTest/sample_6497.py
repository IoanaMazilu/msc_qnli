bus_speed_premise = 50
bus_speed_hypothesis = 50
journey_time_premise = 44
journey_time_hypothesis = 14

# the hypothesis refers to the journey time and speed of the bus mentioned in the premise
if journey_time_premise!= journey_time_hypothesis:
    # check if the journey time in the hypothesis contradicts the journey time reported in the premise
    label = "contradiction"
elif bus_speed_hypothesis!= bus_speed_premise:
    # check if the speed of the bus in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
