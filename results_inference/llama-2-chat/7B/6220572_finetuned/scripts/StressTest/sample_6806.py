distance_premise = 31
distance_hypothesis = 61

# the hypothesis refers to the distance Yolanda and Bob walked, mentioned also in the premise
if distance_hypothesis!= distance_premise:
    # check if the distance in the hypothesis contradicts the distance reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
