driving_distance_premise = 340
driving_distance_hypothesis = 240
driving_speed_premise = 60
driving_speed_hypothesis = 60
driving_distance_next_leg_premise = 120
driving_distance_next_leg_hypothesis = 120
driving_speed_next_leg_premise = 40
driving_speed_next_leg_hypothesis = 40

# the hypothesis refers to the number of driven miles and speed in the premise
if driving_distance_hypothesis!= driving_distance_premise:
    # check if the number of driven miles in the hypothesis contradicts the number of driven miles reported in the premise
    label = "contradiction"
elif driving_speed_hypothesis!= driving_speed_premise:
    # check if the speed in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
elif driving_distance_next_leg_hypothesis!= driving_distance_next_leg_premise:
    # check if the number of driven miles in the next leg in the hypothesis contradicts the number of driven miles reported in the premise
    label = "contradiction"
elif driving_speed_next_leg_hypothesis!= driving_speed_next_leg_premise:
    # check if the speed in the next leg in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
