distance_premise = 40
distance_hypothesis = 10

# the hypothesis refers to the distance from Marathon to Athens mentioned in the premise
if distance_hypothesis >= distance_premise:
    # check if the distance in the hypothesis contradicts the distance mentioned in the premise
    label = "contradiction"
elif distance_hypothesis > distance_premise:
    # check if the distance in the hypothesis is greater than the distance in the premise
    label = "contradiction"
else:
    # if the hypothesis distance does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
