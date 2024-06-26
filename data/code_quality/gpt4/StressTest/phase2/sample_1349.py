investment_premise = 25000
investment_hypothesis = 25000

# the hypothesis refers to the investment made by Mr Shivkumar in 1996, also mentioned in the premise
if investment_hypothesis < investment_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif investment_hypothesis == investment_premise:
    # if the hypothesis value and the premise value are the same, we can infer entailment
    label = "entailment"
else:
    # any other case is considered neutral
    label = "neutral"

print(label)
