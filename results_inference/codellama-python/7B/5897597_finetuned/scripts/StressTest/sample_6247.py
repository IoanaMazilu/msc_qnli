investment_premise = 600000
investment_hypothesis = 100000
interest_rate_premise = 10
interest_rate_hypothesis = 10
period_premise = 3
period_hypothesis = 3

# the hypothesis refers to the amount invested, interest rate and period mentioned in the premise
if investment_hypothesis >= investment_premise:
    # check if the hypothesis value contradicts the estimate of less than 'investment_premise'
    label = "contradiction"
elif interest_rate_hypothesis!= interest_rate_premise or period_hypothesis!= period_premise:
    # check if the interest rate or period in the hypothesis contradicts the ones in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the investment
    # any investment less than 'investment_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
