beat_premise = 1
beat_hypothesis = 1

# the hypothesis mentions the same event as the premise, and the numbers match
if beat_hypothesis == beat_premise:
    # if the hypothesis and premise values match, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis value contradicts the premise value, we can infer contradiction
    label = "contradiction"

print(label)
