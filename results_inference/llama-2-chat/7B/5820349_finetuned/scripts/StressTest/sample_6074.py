first_travel_distance_premise = 8
first_travel_speed_premise = 40
first_stop_time_premise = 15
second_travel_distance_premise = 20
second_travel_speed_premise = 60

first_travel_distance_hypothesis = 5
first_travel_speed_hypothesis = 40
first_stop_time_hypothesis = 15
second_travel_distance_hypothesis = 20
second_travel_speed_hypothesis = 60

# the hypothesis refers to the distances and speeds of Jerry's travels mentioned in the premise
if first_travel_distance_premise!= first_travel_distance_hypothesis:
    # check if the distance of the first travel in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
elif first_travel_speed_premise!= first_travel_speed_hypothesis:
    # check if the speed of the first travel in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
elif first_stop_time_premise!= first_stop_time_hypothesis:
    # check if the stop time in the hypothesis contradicts the stop time reported in the premise
    label = "contradiction"
elif second_travel_distance_premise!= second_travel_distance_hypothesis:
    # check if the distance of the second travel in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
elif second_travel_speed_premise!= second_travel_speed_hypothesis:
    # check if the speed of the second travel in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
