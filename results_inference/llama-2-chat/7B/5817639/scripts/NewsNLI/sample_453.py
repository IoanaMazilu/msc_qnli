range_premise = 60
range_hypothesis = 37

# the hypothesis mentions the same estimated range as the premise
if range_hypothesis == range_premise:
    # if the hypothesis and premise have the same value, we can infer entailment
    label = "entailment"
elif range_hypothesis < range_premise:
    # if the hypothesis value is less than the premise value, we can infer contradiction
    label = "contradiction"
else:
    # if the hypothesis and premise values are different, but not contradictory, we can infer neutrality
    label = "neutral"

print(label)
