butter_weight_premise = 44
butter_weight_hypothesis = 44

# the hypothesis refers to the weight of butter mentioned in the premise
if butter_weight_hypothesis >= butter_weight_premise:
    # check if the hypothesis value contradicts the exact weight of butter in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
