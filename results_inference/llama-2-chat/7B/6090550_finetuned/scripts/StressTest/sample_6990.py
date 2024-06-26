distance_premise = 12 * 2
distance_hypothesis = 52

# the hypothesis refers to the distance the twins ran, which is also mentioned in the premise
if distance_hypothesis < distance_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif distance_hypothesis == distance_premise:
    # if the hypothesis value equals the premise value, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis value is greater than the premise value, it does not contradict the premise, but it cannot be fully entailed either
    label = "neutral"

print(label)
