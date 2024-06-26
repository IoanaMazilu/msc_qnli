first_distance_premise = 240
first_speed_premise = 60
second_distance_premise = 120
second_speed_premise = 40

first_distance_hypothesis = 140
first_speed_hypothesis = 60
second_distance_hypothesis = 120
second_speed_hypothesis = 40

# the hypothesis refers to the distances and speeds mentioned in the premise
if first_distance_hypothesis!= first_distance_premise or first_speed_hypothesis!= first_speed_premise:
    # check if the distances or speeds in the hypothesis contradict the ones reported in the premise
    label = "contradiction"
elif second_distance_hypothesis!= second_distance_premise or second_speed_hypothesis!= second_speed_premise:
    # check if the distances or speeds in the hypothesis contradict the ones reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
