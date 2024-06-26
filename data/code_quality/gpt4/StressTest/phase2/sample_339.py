investment_premise = 120000
investment_hypothesis = 620000

# the hypothesis refers to the amount of investment mentioned in the premise
if investment_hypothesis <= investment_premise:
    # check if the estimate of 'investment_hypothesis' contradicts the amount of investment in the premise
    label = "contradiction"
else:
    # if the hypothesis value is greater than the premise value, it is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
