bus_journey_premise = 44
bus_journey_hypothesis = 14
average_speed_premise = 50
average_speed_hypothesis = 50

# the hypothesis talks about the time taken for the bus journey and the average speed, which are also mentioned in the premise
if bus_journey_hypothesis <= bus_journey_premise:
    # check if the hypothesis value contradicts the estimate of the time taken for the bus journey in the premise
    label = "contradiction"
elif average_speed_hypothesis!= average_speed_premise:
    # check if the average speed in the hypothesis contradicts the average speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
