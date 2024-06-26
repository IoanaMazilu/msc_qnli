investment_premise = 100000
investment_hypothesis = 100000
interest_rate_premise = 10
interest_rate_hypothesis = 10
period_premise = 3
period_hypothesis = 3

# the hypothesis refers to the amount invested, interest rate and period of investment mentioned in the premise
if investment_hypothesis >= investment_premise:
    # check if the estimate of 'investment_hypothesis' contradicts the amount invested in the premise
    label = "contradiction"
elif interest_rate_hypothesis!= interest_rate_premise:
    # check if the interest rate in the hypothesis contradicts the interest rate reported in the premise
    label = "contradiction"
elif period_hypothesis!= period_premise:
    # check if the period of investment in the hypothesis contradicts the period of investment reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)