first_leg_distance_premise = 340
first_leg_speed_premise = 60
second_leg_distance_premise = 120
second_leg_speed_premise = 40

first_leg_distance_hypothesis = 240
first_leg_speed_hypothesis = 60
second_leg_distance_hypothesis = 120
second_leg_speed_hypothesis = 40

# the hypothesis refers to the distance and speed of the first and second legs of Joe's journey mentioned in the premise
if first_leg_distance_hypothesis!= first_leg_distance_premise or second_leg_distance_hypothesis!= second_leg_distance_premise:
    # check if the distances in the hypothesis contradict the distances reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
