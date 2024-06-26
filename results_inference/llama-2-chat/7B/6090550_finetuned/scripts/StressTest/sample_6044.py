distance_premise = 40
distance_hypothesis = 80
maxwell_speed_premise = 4
maxwell_speed_hypothesis = 4
brad_speed_premise = 6
brad_speed_hypothesis = 6

# the hypothesis refers to the distance between homes, Maxwell's speed, and Brad's speed, all mentioned in the premise
if distance_premise!= distance_hypothesis:
    # check if the distance between their homes in the hypothesis contradicts the distance in the premise
    label = "contradiction"
elif maxwell_speed_premise!= maxwell_speed_hypothesis or brad_speed_premise!= brad_speed_hypothesis:
    # check if the speed of Maxwell or Brad in the hypothesis contradicts their speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
