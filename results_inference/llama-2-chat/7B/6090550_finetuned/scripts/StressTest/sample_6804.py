distance_premise = 31
distance_hypothesis = 81

# the hypothesis refers to the distance Yolanda walked, which is also mentioned in the premise
if distance_premise >= distance_hypothesis:
    # check if the distance in the hypothesis contradicts the distance in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
