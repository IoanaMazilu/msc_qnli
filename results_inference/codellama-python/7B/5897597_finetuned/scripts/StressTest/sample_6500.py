distance_premise = 45
distance_hypothesis = 45

# the hypothesis refers to the same distance mentioned in the premise
if distance_hypothesis <= distance_premise:
    # check if the hypothesis value contradicts the exact distance in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
