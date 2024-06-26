distance_premise = 15
distance_hypothesis = 85

# the hypothesis refers to the distance between West-Town and East-Town mentioned in the premise
if distance_hypothesis < distance_premise:
    # check if the estimate of 'distance_hypothesis' contradicts the distance reported in the premise
    label = "contradiction"
elif distance_hypothesis == distance_premise:
    # if the hypothesis value equals the premise one, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis estimate does not contradict the premise one, but also doesn't equal it, we have a neutral case
    label = "neutral"

print(label)
