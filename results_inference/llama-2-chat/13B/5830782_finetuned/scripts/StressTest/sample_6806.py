distance_premise = 31
distance_hypothesis = 61

# the hypothesis refers to the distance between X and Y mentioned in the premise
if distance_premise!= distance_hypothesis:
    # check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the distance in the hypothesis does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
