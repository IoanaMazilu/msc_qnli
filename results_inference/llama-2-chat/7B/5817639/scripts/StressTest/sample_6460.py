investment_premise = 72500
investment_hypothesis = 62500

# the hypothesis refers to the amount of money deposited in the investment fund mentioned in the premise
if investment_hypothesis <= investment_premise:
    # check if the estimate of 'investment_hypothesis' contradicts the amount of money deposited in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money deposited
    # any amount of money greater than 'investment_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
