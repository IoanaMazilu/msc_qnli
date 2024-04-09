first_travel_distance_premise = 8
first_travel_distance_hypothesis = 5
first_travel_speed_premise = 40
first_travel_speed_hypothesis = 40
stop_time_premise = 15
stop_time_hypothesis = 15
second_travel_distance_premise = 20
second_travel_distance_hypothesis = 20
second_travel_speed_premise = 60
second_travel_speed_hypothesis = 60

# the hypothesis talks about the same travel distances, speeds, and stop time as the premise
if first_travel_distance_hypothesis!= first_travel_distance_premise:
    # check if the distance travelled in the first leg of the trip in the hypothesis contradicts the distance travelled in the first leg of the trip in the premise
    label = "contradiction"
elif first_travel_speed_hypothesis!= first_travel_speed_premise:
    # check if the speed of travel in the first leg of the trip in the hypothesis contradicts the speed of travel in the first leg of the trip in the premise
    label = "contradiction"
elif stop_time_hypothesis!= stop_time_premise:
    # check if the stop time in the hypothesis contradicts the stop time in the premise
    label = "contradiction"
elif second_travel_distance_hypothesis!= second_travel_distance_premise:
    # check if the distance travelled in the second leg of the trip in the hypothesis contradicts the distance travelled in the second leg of the trip in the premise
    label = "contradiction"
elif second_travel_speed_hypothesis!= second_travel_speed_premise:
    # check if the speed of travel in the second leg of the trip in the hypothesis contradicts the speed of travel in the second leg of the trip in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
