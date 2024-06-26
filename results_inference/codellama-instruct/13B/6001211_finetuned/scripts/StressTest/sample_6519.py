first_distance_premise = 8
first_distance_hypothesis = 5
first_speed_premise = 40
first_speed_hypothesis = 40
stop_time_premise = 14
stop_time_hypothesis = 14
second_distance_premise = 20
second_distance_hypothesis = 20
second_speed_premise = 60
second_speed_hypothesis = 60

# the hypothesis refers to the distances and speeds mentioned in the premise
if first_distance_premise <= first_distance_hypothesis:
    # check if the estimate of 'first_distance_hypothesis' contradicts the distance travelled in the premise
    label = "contradiction"
elif first_speed_premise!= first_speed_hypothesis:
    # check if the speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
elif stop_time_premise!= stop_time_hypothesis:
    # check if the stop time in the hypothesis contradicts the stop time reported in the premise
    label = "contradiction"
elif second_distance_premise!= second_distance_hypothesis:
    # check if the second distance in the hypothesis contradicts the second distance reported in the premise
    label = "contradiction"
elif second_speed_premise!= second_speed_hypothesis:
    # check if the second speed in the hypothesis contradicts the second speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
