investment_premise = 100000000
investment_hypothesis = 100000000

# the hypothesis mentions the same amount of investment as the premise
if investment_hypothesis!= investment_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is the same as the premise value, we can infer entailment
    label = "entailment"

print(label)
