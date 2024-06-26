investment_rate_premise = 2
investment_rate_hypothesis = 8

# the hypothesis talks about the investment rate of Sandy, referenced also in the premise
if investment_rate_hypothesis <= investment_rate_premise:
    # check if the hypothesis value contradicts the estimate of more than 'investment_rate_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the investment rate
    # any investment rate greater than 'investment_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
