miles_first_trip_premise = 8
miles_first_trip_hypothesis = 6
speed_first_trip_premise = 40
speed_first_trip_hypothesis = 40
stop_time_premise = 11
stop_time_hypothesis = 11
miles_second_trip_premise = 20
miles_second_trip_hypothesis = 20
speed_second_trip_premise = 60
speed_second_trip_hypothesis = 60

# the hypothesis refers to the same travels, stops and speeds as the premise
if miles_first_trip_hypothesis!= miles_first_trip_premise:
    # check if the distance traveled in the first trip in the hypothesis contradicts the distance traveled in the first trip reported in the premise
    label = "contradiction"
elif speed_first_trip_hypothesis!= speed_first_trip_premise:
    # check if the speed of travel in the first trip in the hypothesis contradicts the speed of travel in the first trip reported in the premise
    label = "contradiction"
elif stop_time_hypothesis!= stop_time_premise:
    # check if the stop time in the hypothesis contradicts the stop time reported in the premise
    label = "contradiction"
elif miles_second_trip_hypothesis!= miles_second_trip_premise:
    # check if the distance traveled in the second trip in the hypothesis contradicts the distance traveled in the second trip reported in the premise
    label = "contradiction"
elif speed_second_trip_hypothesis!= speed_second_trip_premise:
    # check if the speed of travel in the second trip in the hypothesis contradicts the speed of travel in the second trip reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
