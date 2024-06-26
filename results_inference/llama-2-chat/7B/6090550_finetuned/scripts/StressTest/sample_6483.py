distance_homes_premise = 20
distance_homes_hypothesis = 80
maxwell_speed_premise = 4
maxwell_speed_hypothesis = 4
brad_speed_premise = 6
brad_speed_hypothesis = 6

# the hypothesis refers to the distance between their homes, Maxwell's speed, and Brad's speed, all mentioned in the premise
if distance_homes_hypothesis <= distance_homes_premise:
    # check if the distance between their homes in the hypothesis contradicts the premise
    label = "contradiction"
elif maxwell_speed_hypothesis!= maxwell_speed_premise or brad_speed_hypothesis!= brad_speed_premise:
    # check if Maxwell's speed or Brad's speed in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
