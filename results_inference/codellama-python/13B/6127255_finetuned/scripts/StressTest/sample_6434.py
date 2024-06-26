investment_premise = 8000
investment_hypothesis = 2000
years_premise = 2
years_hypothesis = 2
interest_rate_premise = 5
interest_rate_hypothesis = 5

# the hypothesis refers to the same investment, years and interest rate as the premise
if investment_hypothesis!= investment_premise:
    # check if the investment amount in the hypothesis contradicts the investment amount in the premise
    label = "contradiction"
elif years_hypothesis!= years_premise or interest_rate_hypothesis!= interest_rate_premise:
    # check if the years or interest rate in the hypothesis contradicts the years or interest rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
