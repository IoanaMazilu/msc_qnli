bus_journey_premise = 44
bus_journey_hypothesis = 24
average_speed_premise = 50
average_speed_hypothesis = 50

# the hypothesis refers to the time and average speed of the bus journey mentioned in the premise
if bus_journey_hypothesis <= bus_journey_premise:
    # check if the estimate of 'bus_journey_hypothesis' contradicts the time of the bus journey in the premise
    label = "contradiction"
elif average_speed_hypothesis!= average_speed_premise:
    # check if the average speed in the hypothesis contradicts the average speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
