first_leg_distance_premise = 8
first_leg_distance_hypothesis = 5
first_leg_speed_premise = 40
first_leg_speed_hypothesis = 40
stop_time_premise = 14
stop_time_hypothesis = 14
second_leg_distance_premise = 20
second_leg_distance_hypothesis = 20
second_leg_speed_premise = 60
second_leg_speed_hypothesis = 60

# the hypothesis refers to the same travel distances and speeds mentioned in the premise
if first_leg_distance_premise <= first_leg_distance_hypothesis:
    # check if the estimate of 'first_leg_distance_hypothesis' contradicts the first leg distance in the premise
    label = "contradiction"
elif first_leg_speed_premise!= first_leg_speed_hypothesis:
    # check if the first leg speed in the hypothesis contradicts the first leg speed reported in the premise
    label = "contradiction"
elif stop_time_premise!= stop_time_hypothesis:
    # check if the stop time in the hypothesis contradicts the stop time reported in the premise
    label = "contradiction"
elif second_leg_distance_premise!= second_leg_distance_hypothesis:
    # check if the second leg distance in the hypothesis contradicts the second leg distance reported in the premise
    label = "contradiction"
elif second_leg_speed_premise!= second_leg_speed_hypothesis:
    # check if the second leg speed in the hypothesis contradicts the second leg speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
