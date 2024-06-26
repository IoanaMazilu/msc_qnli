first_travel_distance_premise = 8
first_travel_distance_hypothesis = 8
first_travel_speed_premise = 40
first_travel_speed_hypothesis = 40
stop_time_premise = 14
stop_time_hypothesis = 14
second_travel_distance_premise = 20
second_travel_distance_hypothesis = 20
second_travel_speed_premise = 60
second_travel_speed_hypothesis = 60

# the hypothesis refers to the exact same situation as the premise, with the same distances, speeds and stop time
if first_travel_distance_hypothesis >= first_travel_distance_premise:
    # check if the 'less than first_travel_distance_hypothesis' contradicts the distance traveled in the premise
    label = "contradiction"
elif first_travel_speed_hypothesis != first_travel_speed_premise or second_travel_speed_hypothesis != second_travel_speed_premise:
    # check if the speeds in the hypothesis contradict the speeds in the premise
    label = "contradiction"
elif stop_time_hypothesis != stop_time_premise or second_travel_distance_hypothesis != second_travel_distance_premise:
    # check if the stop time or the second traveled distance in the hypothesis contradict the same values in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
