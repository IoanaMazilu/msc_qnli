investment_premise = 5000
investment_hypothesis = 8000
interest_rate_premise = 5
interest_rate_hypothesis = 5
deposit_period_premise = 2
deposit_period_hypothesis = 2

# the hypothesis refers to the amount invested, the interest rate and the deposit period mentioned in the premise
if investment_hypothesis <= investment_premise:
    # check if the hypothesis value contradicts the estimate of more than 'investment_premise'
    label = "contradiction"
elif interest_rate_hypothesis!= interest_rate_premise or deposit_period_hypothesis!= deposit_period_premise:
    # check if the interest rate or the deposit period in the hypothesis contradicts the ones reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the investment
    # any investment greater than 'investment_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
