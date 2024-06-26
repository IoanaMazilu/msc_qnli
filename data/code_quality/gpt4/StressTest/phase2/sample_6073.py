first_travel_distance_premise = 7
first_travel_speed_premise = 40
stop_time_premise = 15
second_travel_distance_premise = 20
second_travel_speed_premise = 60

first_travel_distance_hypothesis = 8
first_travel_speed_hypothesis = 40
stop_time_hypothesis = 15
second_travel_distance_hypothesis = 20
second_travel_speed_hypothesis = 60

# the hypothesis describes the same journey as the premise, providing exact values for the distances, speeds and stop time
if first_travel_distance_hypothesis <= first_travel_distance_premise:
    # check if the hypothesis distance contradicts the estimate of more than 'first_travel_distance_premise' miles
    label = "contradiction"
elif first_travel_speed_hypothesis != first_travel_speed_premise or second_travel_speed_hypothesis != second_travel_speed_premise:
    # check if the speeds given in the hypothesis contradict the speeds given in the premise
    label = "contradiction"
elif stop_time_hypothesis != stop_time_premise:
    # check if the stop time given in the hypothesis contradicts the stop time given in the premise
    label = "contradiction"
elif second_travel_distance_hypothesis != second_travel_distance_premise:
    # check if the second travel distance given in the hypothesis contradicts the second travel distance given in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
