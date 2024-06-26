investment_premise = 8000
investment_hypothesis = 2000
interest_rate_premise = 5
interest_rate_hypothesis = 5

# the hypothesis refers to the investment amount and interest rate mentioned in the premise
if investment_premise!= investment_hypothesis:
    # check if the investment amount in the hypothesis contradicts the investment amount reported in the premise
    label = "contradiction"
elif interest_rate_premise!= interest_rate_hypothesis:
    # check if the interest rate in the hypothesis contradicts the interest rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
