real_madrid_premise = 5
real_madrid_hypothesis = 5

# the hypothesis mentions the score of the match, which is also referenced in the premise
if real_madrid_hypothesis == real_madrid_premise:
    # if the hypothesis value matches the premise value, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis value does not match the premise value, we can infer contradiction or neutrality
    if real_madrid_hypothesis > real_madrid_premise:
        label = "contradiction"
    else:
        label = "neutral"

print(label)
