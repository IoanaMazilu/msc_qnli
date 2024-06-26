distance_1_premise = 240
speed_1_premise = 60
distance_2_premise = 120
speed_2_premise = 40
distance_1_hypothesis = 140
speed_1_hypothesis = 60
distance_2_hypothesis = 120
speed_2_hypothesis = 40

# the hypothesis talks about the distances and speeds Joe drives at, referenced also in the premise
if distance_1_hypothesis!= distance_1_premise or speed_1_hypothesis!= speed_1_premise:
    # check if the distances or speeds in the first part of the hypothesis contradict the premise
    label = "contradiction"
elif distance_2_hypothesis!= distance_2_premise or speed_2_hypothesis!= speed_2_premise:
    # check if the distances or speeds in the second part of the hypothesis contradict the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
