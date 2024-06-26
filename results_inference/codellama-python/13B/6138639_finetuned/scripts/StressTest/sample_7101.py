distance_1_premise = 240
distance_1_hypothesis = 340
speed_1_premise = 60
speed_1_hypothesis = 60
distance_2_premise = 120
distance_2_hypothesis = 120
speed_2_premise = 40
speed_2_hypothesis = 40

# the hypothesis refers to the distances and speeds mentioned in the premise
if distance_1_premise > distance_1_hypothesis:
    # check if the distance in the hypothesis contradicts the distance in the premise
    label = "contradiction"
elif speed_1_premise!= speed_1_hypothesis:
    # check if the speed in the hypothesis contradicts the speed in the premise
    label = "contradiction"
elif distance_2_premise!= distance_2_hypothesis:
    # check if the distance in the hypothesis contradicts the distance in the premise
    label = "contradiction"
elif speed_2_premise!= speed_2_hypothesis:
    # check if the speed in the hypothesis contradicts the speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
