investment_premise = 50000
investment_hypothesis = 10000

# the hypothesis refers to the amount of investment mentioned in the premise
if investment_hypothesis <= investment_premise:
    # check if the hypothesis value contradicts the amount of investment in the premise
    label = "contradiction"
else:
    # any amount of investment greater than 'investment_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
