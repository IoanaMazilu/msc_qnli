investment_fund_premise = 62500
investment_fund_hypothesis = float(45000)

# the hypothesis talks about the amount deposited in an investment fund, referenced also in the premise
if investment_fund_hypothesis <= investment_fund_premise:
    # check if the hypothesis value contradicts the estimate of more than 'investment_fund_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount deposited
    # any amount deposited greater than 'investment_fund_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
