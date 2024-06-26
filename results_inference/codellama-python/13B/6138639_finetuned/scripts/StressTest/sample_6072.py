distance_travelled_premise = 8 + 20
distance_travelled_hypothesis = 7
stop_time_premise = 15
stop_time_hypothesis = 15

# the hypothesis refers to the total distance travelled, the stop time and the average speed mentioned in the premise
if distance_travelled_premise <= distance_travelled_hypothesis:
    # check if the estimate of 'distance_travelled_hypothesis' contradicts the total distance travelled in the premise
    label = "contradiction"
elif stop_time_hypothesis!= stop_time_premise:
    # check if the stop time in the hypothesis contradicts the stop time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
