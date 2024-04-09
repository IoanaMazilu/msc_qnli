months_later_premise = 4
investment_premise = 90000
investment_hypothesis = float(90000) + 1

# the hypothesis talks about the investment amount more than the premise
if investment_hypothesis >= investment_premise:
    # check if the hypothesis value contradicts the estimate of the investment amount in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the investment amount
    # any investment amount greater than the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
