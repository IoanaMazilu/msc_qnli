distance_premise = 45
distance_hypothesis = 85

# the hypothesis refers to the distance between the same points mentioned in the premise
if distance_hypothesis!= distance_premise:
    # check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
