distance_premise = 12
distance_hypothesis = 52

# the hypothesis refers to the distance the twins ran, which is also mentioned in the premise
if distance_hypothesis < distance_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
