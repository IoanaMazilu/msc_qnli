first_distance_premise = 8
first_distance_hypothesis = 8
first_speed_premise = 40
first_speed_hypothesis = 40
stop_time_premise = 12
stop_time_hypothesis = 12
second_distance_premise = 20
second_distance_hypothesis = 20
second_speed_premise = 60
second_speed_hypothesis = 60

# the hypothesis talks about Jerry's travel distances, speeds, and stop time, which are also referenced in the premise
if first_distance_hypothesis >= first_distance_premise:
    # check if the hypothesis value contradicts the premise of Jerry travelling 8 miles at first
    label = "contradiction"
elif first_speed_hypothesis != first_speed_premise or stop_time_hypothesis != stop_time_premise or second_distance_hypothesis != second_distance_premise or second_speed_hypothesis != second_speed_premise:
    # check if any other values in the hypothesis contradict the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
