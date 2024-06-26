distance_premise = 20
distance_hypothesis = 80
speed_maxwell = 4
speed_brad = 6

# the hypothesis refers to the distance between their homes, Maxwell's walking speed and Brad's running speed, which are also mentioned in the premise
if distance_hypothesis <= distance_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
