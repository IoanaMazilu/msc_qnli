investment_premise = 7000000
investment_hypothesis = 1000000
interest_rate_premise = 10
interest_rate_hypothesis = 10
period_premise = 3
period_hypothesis = 3

# the hypothesis talks about the investment amount, interest rate and investment period, referenced also in the premise
if investment_hypothesis >= investment_premise:
    # check if the hypothesis value contradicts the estimate of less than 'investment_premise'
    label = "contradiction"
elif interest_rate_hypothesis != interest_rate_premise or period_hypothesis != period_premise:
    # check if the interest rate or the investment period in the hypothesis contradicts the ones in the premise
    label = "contradiction"
else:
    # the premise gives only an upper limit for the investment amount
    # any investment amount less than 'investment_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
