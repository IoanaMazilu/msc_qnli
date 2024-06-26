scott_golf_premise = 38
scott_golf_hypothesis = 37.5

# the hypothesis refers to the average golf score on the first four rounds
if scott_golf_hypothesis < scott_golf_premise:
    # the hypothesis value is less than the premise value, so we can infer entailment
    label = "entailment"
elif scott_golf_hypothesis > scott_golf_premise:
    # the hypothesis value is greater than the premise value, so we can infer contradiction
    label = "contradiction"
else:
    # the hypothesis value is equal to the premise value, so we cannot infer entailment or contradiction
    label = "neutral"

print(label)
