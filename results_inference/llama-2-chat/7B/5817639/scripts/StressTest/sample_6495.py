bus_journey_premise = 44
bus_journey_hypothesis = 24
bus_speed_premise = 50
bus_speed_hypothesis = 50

# the hypothesis refers to the time taken to reach Pune and the average speed of the bus, which are also mentioned in the premise
if bus_journey_hypothesis <= bus_journey_premise:
    # check if the hypothesis value contradicts the estimate of 'bus_journey_premise'
    label = "contradiction"
elif bus_speed_hypothesis!= bus_speed_premise:
    # check if the estimated speed of the bus in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
