distance_premise = 31
distance_hypothesis = 81

# the hypothesis refers to the distance Yolanda and Bob walked, which is also mentioned in the premise
if distance_hypothesis <= distance_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
