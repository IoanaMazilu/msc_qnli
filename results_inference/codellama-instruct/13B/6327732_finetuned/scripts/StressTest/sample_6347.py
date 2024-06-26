investment_premise = 50000
investment_hypothesis = 50000

# the hypothesis refers to the investment amount mentioned in the premise
if investment_hypothesis >= investment_premise:
    # check if the estimate of 'investment_hypothesis' contradicts the investment amount in the premise
    label = "contradiction"
else:
    # the premise gives an exact investment amount
    # any investment amount less than 'investment_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
