distance_yolanda = 31
distance_hypothesis = 61

# the hypothesis refers to the distance Yolanda walked, which is also mentioned in the premise
if distance_yolanda!= distance_hypothesis:
    # check if the distance Yolanda walked in the hypothesis contradicts the distance mentioned in the premise
    label = "contradiction"
else:
    # if the distance Yolanda walked in the hypothesis matches the distance in the premise, we can infer entailment
    label = "entailment"

print(label)
