first_leg_distance_premise = 8
first_leg_speed_premise = 40
second_leg_distance_premise = 20
second_leg_speed_premise = 60
stop_time_premise = 15

first_leg_distance_hypothesis = 5
first_leg_speed_hypothesis = 40
second_leg_distance_hypothesis = 20
second_leg_speed_hypothesis = 60
stop_time_hypothesis = 15

# the hypothesis refers to the same traveling distances and speeds as the premise
if first_leg_distance_hypothesis!= first_leg_distance_premise or first_leg_speed_hypothesis!= first_leg_speed_premise:
    # check if the first leg's distance or speed in the hypothesis contradicts the premise
    label = "contradiction"
elif second_leg_distance_hypothesis!= second_leg_distance_premise or second_leg_speed_hypothesis!= second_leg_speed_premise:
    # check if the second leg's distance or speed in the hypothesis contradicts the premise
    label = "contradiction"
elif stop_time_hypothesis!= stop_time_premise:
    # check if the stop time in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
