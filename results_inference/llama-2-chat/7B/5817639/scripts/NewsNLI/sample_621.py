chance_premise = 0.4
chance_hypothesis = 0.4

# the hypothesis mentions the same probability as the premise
if chance_hypothesis == chance_premise:
    # if the hypothesis value matches the premise value, we can infer entailment
    label = "entailment"
else:
    # if the hypothesis value contradicts the premise value, we can infer contradiction
    label = "contradiction"

print(label)
