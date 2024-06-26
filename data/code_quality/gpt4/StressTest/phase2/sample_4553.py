distance_walked_premise = 8
distance_walked_hypothesis = 8

# the hypothesis refers to the distance Jack walked, which is mentioned in the premise
if distance_walked_hypothesis > distance_walked_premise:
    # check if the distance in the hypothesis contradicts the distance mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
