investment_fund_premise = 62500
investment_fund_hypothesis = 52500

# the hypothesis talks about the amount deposited in an investment fund, which is also mentioned in the premise
if investment_fund_hypothesis <= investment_fund_premise:
    # check if the hypothesis value contradicts the estimate of the deposited amount in the premise
    label = "contradiction"
else:
    # the premise provides an estimate for the amount deposited, which can be entailed from the premise
    label = "entailment"

print(label)
