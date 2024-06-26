distance_premise = 2
distance_hypothesis = 3

# the hypothesis refers to the distance run by the twins, which is also mentioned in the premise
if distance_hypothesis < distance_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif distance_hypothesis == distance_premise:
    # if the hypothesis value equals the premise value, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis value is greater than the premise value, we can infer entailment
    label = "entailment"

print(label)
