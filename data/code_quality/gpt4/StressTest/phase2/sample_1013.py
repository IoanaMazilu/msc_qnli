distance_premise = 110
speed_maxwell_premise = 4
speed_brad_premise = 7
distance_hypothesis = 110
speed_maxwell_hypothesis = 4
speed_brad_hypothesis = 7

# the hypothesis refers to the distance between the homes, and the walking and running speeds of Maxwell and Brad, respectively
if distance_hypothesis > distance_premise:
    # check if the distance in the hypothesis contradicts the distance in the premise
    label = "contradiction"
elif speed_maxwell_hypothesis != speed_maxwell_premise or speed_brad_hypothesis != speed_brad_premise:
    # check if the speeds in the hypothesis contradict the speeds in the premise
    label = "contradiction"
else:
    # if the distance and speeds in the hypothesis do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
