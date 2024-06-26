distance_premise = 52
distance_hypothesis = 62

# the hypothesis refers to the same distance mentioned in the premise
if distance_hypothesis < distance_premise:
    # check if the hypothesis value contradicts the distance reported in the premise
    label = "contradiction"
elif distance_hypothesis > distance_premise:
    # check if the hypothesis value is more than the distance reported in the premise
    label = "neutral"
else:
    # if the hypothesis value and the premise value are the same, we can infer entailment
    label = "entailment"

print(label)
