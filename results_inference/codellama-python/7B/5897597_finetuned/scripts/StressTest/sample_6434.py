investment_premise = 8000
investment_hypothesis = 2000
interest_rate_premise = 5
interest_rate_hypothesis = 5
deposit_period_premise = 2
deposit_period_hypothesis = 2

# the hypothesis refers to the amount invested, the interest rate and the deposit period mentioned in the premise
if investment_hypothesis!= investment_premise:
    # check if the amount invested in the hypothesis contradicts the amount invested in the premise
    label = "contradiction"
elif interest_rate_hypothesis!= interest_rate_premise:
    # check if the interest rate in the hypothesis contradicts the interest rate in the premise
    label = "contradiction"
elif deposit_period_hypothesis!= deposit_period_premise:
    # check if the deposit period in the hypothesis contradicts the deposit period in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
