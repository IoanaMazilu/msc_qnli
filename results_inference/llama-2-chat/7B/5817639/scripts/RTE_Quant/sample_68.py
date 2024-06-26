dollar_premise = 3
dollar_hypothesis = 3

# the hypothesis talks about the cost of the first Barbie doll, which is also mentioned in the premise
if dollar_hypothesis == dollar_premise:
    # if the hypothesis and premise values are the same, we can infer entailment
    label = "entailment"
elif dollar_hypothesis < dollar_premise:
    # if the hypothesis value is less than the premise value, we can infer contradiction
    label = "contradiction"
else:
    # if the hypothesis and premise values are not the same and cannot be compared, we can infer neutrality
    label = "neutral"

print(label)
