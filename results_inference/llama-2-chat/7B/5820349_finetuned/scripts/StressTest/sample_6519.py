first_travel_distance_premise = 8
first_travel_distance_hypothesis = 5
second_travel_distance_premise = 20
second_travel_distance_hypothesis = 20
average_speed_premise = 40
average_speed_hypothesis = 40
stop_time_premise = 14
stop_time_hypothesis = 14

# the hypothesis refers to the same travel distances, average speed and stop time mentioned in the premise
if first_travel_distance_premise <= first_travel_distance_hypothesis:
    # check if the estimate of 'first_travel_distance_hypothesis' contradicts the first travel distance in the premise
    label = "contradiction"
elif second_travel_distance_hypothesis!= second_travel_distance_premise or average_speed_hypothesis!= average_speed_premise or stop_time_hypothesis!= stop_time_premise:
    # check if the other travel distances, average speed and stop time in the hypothesis contradict the ones reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
