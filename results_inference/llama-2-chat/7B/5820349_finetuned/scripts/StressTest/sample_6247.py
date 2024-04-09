investment_premise = 600000
investment_hypothesis = 100000
interest_rate_premise = 10
interest_rate_hypothesis = 10
investment_period_premise = 3
investment_period_hypothesis = 3

# the hypothesis refers to the amount of investment, interest rate, and investment period mentioned in the premise
if investment_hypothesis >= investment_premise:
    # check if the amount of investment in the hypothesis contradicts the premise of less than 'investment_premise'
    label = "contradiction"
elif interest_rate_hypothesis!= interest_rate_premise or investment_period_hypothesis!= investment_period_premise:
    # check if the interest rate or investment period in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of investment
    # any amount of investment less than 'investment_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
