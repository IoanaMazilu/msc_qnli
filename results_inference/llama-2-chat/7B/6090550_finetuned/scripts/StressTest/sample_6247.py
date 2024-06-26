invested_amount_premise = 600000
invested_amount_hypothesis = 100000
interest_rate_premise = 10
interest_rate_hypothesis = 10
period_premise = 3
period_hypothesis = 3

# the hypothesis talks about the investment amount, interest rate and period, all referenced in the premise
if invested_amount_hypothesis >= invested_amount_premise:
    # check if the hypothesis value contradicts the estimate of less than 'invested_amount_premise'
    label = "contradiction"
elif interest_rate_hypothesis!= interest_rate_premise or period_hypothesis!= period_premise:
    # check if the interest rate or period in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the hypothesis values do not contradict the premise ones
    label = "neutral"

print(label)
