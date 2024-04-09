first_leg_distance_premise = 240
first_leg_speed_premise = 60
second_leg_distance_premise = 120
second_leg_speed_premise = 40

first_leg_distance_hypothesis = 140
first_leg_speed_hypothesis = 60
second_leg_distance_hypothesis = 120
second_leg_speed_hypothesis = 40

# the hypothesis refers to the distances and speeds of the two legs of driving mentioned in the premise
if first_leg_distance_premise!= first_leg_distance_hypothesis:
    # check if the distance of the first leg in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
elif first_leg_speed_premise!= first_leg_speed_hypothesis:
    # check if the speed of the first leg in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
elif second_leg_distance_premise!= second_leg_distance_hypothesis:
    # check if the distance of the second leg in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
elif second_leg_speed_premise!= second_leg_speed_hypothesis:
    # check if the speed of the second leg in the hypothesis contradicts the speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
