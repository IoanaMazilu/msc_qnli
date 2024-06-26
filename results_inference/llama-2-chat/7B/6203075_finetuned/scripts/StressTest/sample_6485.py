distance_premise = 20
distance_hypothesis = 20
maxwell_speed = 4
brad_speed = 6

# the hypothesis refers to the distance between their homes, Maxwell's speed, and Brad's speed
if distance_hypothesis <= distance_premise:
    # check if the distance in the hypothesis contradicts the distance in the premise
    label = "entailment"
elif maxwell_speed!= 4 or brad_speed!= 6:
    # check if the speed of Maxwell or Brad in the hypothesis contradicts their speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "neutral"

print(label)