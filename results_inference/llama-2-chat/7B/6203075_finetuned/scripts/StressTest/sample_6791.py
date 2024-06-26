distance_premise = 50
distance_hypothesis = 50
maxwell_speed = 4
brad_speed = 6

# the hypothesis refers to the distance between their homes, Maxwell's speed and Brad's speed mentioned in the premise
if distance_hypothesis <= distance_premise:
    # check if the hypothesis value contradicts the premise of more than 'distance_premise'
    label = "entailment"
elif maxwell_speed!= 4 or brad_speed!= 6:
    # check if the speed of Maxwell or Brad contradicts the speed in the premise
    label = "contradiction"
else:
    # if the hypothesis values and speeds do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)
