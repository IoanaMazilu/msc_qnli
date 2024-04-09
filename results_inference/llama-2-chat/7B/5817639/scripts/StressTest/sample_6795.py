investment_fund_premise = 62500
investment_fund_hypothesis = 22500

# the hypothesis talks about the amount deposited in an investment fund, referenced also in the premise
if investment_fund_hypothesis <= investment_fund_premise:
    # check if the hypothesis value contradicts the estimate of 'investment_fund_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount deposited
    # any amount greater than 'investment_fund_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
