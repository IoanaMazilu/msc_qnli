first_travel_distance_premise = 8
first_travel_distance_hypothesis = 6
first_travel_speed_premise = 40
first_travel_speed_hypothesis = 40
first_stop_time_premise = 11
first_stop_time_hypothesis = 11
second_travel_distance_premise = 20
second_travel_distance_hypothesis = 20
second_travel_speed_premise = 60
second_travel_speed_hypothesis = 60

# the hypothesis refers to the same travel, stop and second travel distances and times as the premise
if first_travel_distance_premise!= first_travel_distance_hypothesis:
    # check if the distance travelled in the first leg of the journey in the hypothesis contradicts the premise
    label = "contradiction"
elif first_travel_speed_premise!= first_travel_speed_hypothesis:
    # check if the speed of travel in the first leg of the journey in the hypothesis contradicts the premise
    label = "contradiction"
elif first_stop_time_premise!= first_stop_time_hypothesis:
    # check if the stop time in the first leg of the journey in the hypothesis contradicts the premise
    label = "contradiction"
elif second_travel_distance_premise!= second_travel_distance_hypothesis:
    # check if the distance travelled in the second leg of the journey in the hypothesis contradicts the premise
    label = "contradiction"
elif second_travel_speed_premise!= second_travel_speed_hypothesis:
    # check if the speed of travel in the second leg of the journey in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
