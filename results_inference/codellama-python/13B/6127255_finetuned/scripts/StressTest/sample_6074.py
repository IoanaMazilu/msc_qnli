first_travel_distance_premise = 8
first_travel_speed_premise = 40
stop_time_premise = 15
second_travel_distance_premise = 20
second_travel_speed_premise = 60

first_travel_distance_hypothesis = 5
first_travel_speed_hypothesis = 40
stop_time_hypothesis = 15
second_travel_distance_hypothesis = 20
second_travel_speed_hypothesis = 60

# the hypothesis refers to the travel distances, speeds and stop times mentioned in the premise
if first_travel_distance_hypothesis!= first_travel_distance_premise:
    # check if the distance travelled at the first speed in the hypothesis contradicts the distance travelled at the first speed in the premise
    label = "contradiction"
elif first_travel_speed_hypothesis!= first_travel_speed_premise:
    # check if the speed of the first travel in the hypothesis contradicts the speed of the first travel in the premise
    label = "contradiction"
elif stop_time_hypothesis!= stop_time_premise:
    # check if the stop time in the hypothesis contradicts the stop time in the premise
    label = "contradiction"
elif second_travel_distance_hypothesis!= second_travel_distance_premise:
    # check if the distance travelled at the second speed in the hypothesis contradicts the distance travelled at the second speed in the premise
    label = "contradiction"
elif second_travel_speed_hypothesis!= second_travel_speed_premise:
    # check if the speed of the second travel in the hypothesis contradicts the speed of the second travel in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
