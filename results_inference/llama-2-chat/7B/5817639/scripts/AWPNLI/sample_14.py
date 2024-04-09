oranges_premise = 37.0
oranges_hypothesis = 47.0

# the hypothesis refers to the total number of oranges picked, which is also mentioned in the premise
# compare the estimated number of oranges in the hypothesis with the premise value
if oranges_hypothesis == oranges_premise:
    # if the hypothesis value matches the premise value, we can infer entailment
    label = "entailment"
elif oranges_hypothesis > oranges_premise:
    # if the hypothesis value is greater than the premise value, we can infer contradiction
    label = "contradiction"
else:
    # if the hypothesis value is equal to the premise value, we cannot infer entailment or contradiction
    label = "neutral"

print(label)
