distance_premise = 20
distance_hypothesis = 80
maxwell_speed_premise = 4
maxwell_speed_hypothesis = 4
brad_speed_premise = 6
brad_speed_hypothesis = 6

# the hypothesis refers to the distance between their homes, Maxwell's walking speed, and Brad's running speed, which are also mentioned in the premise
if distance_hypothesis <= distance_premise:
    # check if the hypothesis value contradicts the distance value in the premise
    label = "contradiction"
elif maxwell_speed_hypothesis!= maxwell_speed_premise or brad_speed_hypothesis!= brad_speed_premise:
    # check if the speed values in the hypothesis contradict the speed values in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
