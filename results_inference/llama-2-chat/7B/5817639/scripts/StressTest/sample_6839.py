earnings_premise = 9000
earnings_hypothesis = 9000

# the hypothesis talks about the amount of money earned by the person and Rick, referenced also in the premise
if earnings_hypothesis == earnings_premise:
    # if the hypothesis value is equal to the premise value, we can infer entailment
    label = "entailment"
elif earnings_hypothesis < earnings_premise:
    # if the hypothesis value is less than the premise value, we can infer contradiction
    label = "contradiction"
else:
    # if the hypothesis value is greater than or equal to the premise value, but does not match exactly, we can infer neutrality
    label = "neutral"

print(label)
