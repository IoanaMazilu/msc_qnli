bus_journey_time_premise = 44
bus_journey_time_hypothesis = 24
bus_speed_premise = 50
bus_speed_hypothesis = 50

# the hypothesis refers to the time taken by the bus to reach Pune and its average speed, which are also mentioned in the premise
if bus_journey_time_hypothesis <= bus_journey_time_premise:
    # check if the hypothesis value contradicts the estimate of more than 'bus_journey_time_premise'
    label = "contradiction"
elif bus_speed_hypothesis!= bus_speed_premise:
    # check if the average speed of the bus in the hypothesis contradicts the average speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
