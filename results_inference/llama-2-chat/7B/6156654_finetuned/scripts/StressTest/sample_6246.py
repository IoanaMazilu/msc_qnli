investment_amount_premise = 100000
investment_amount_hypothesis = 600000
interest_rate_premise = 10
interest_rate_hypothesis = 10
time_period_premise = 3
time_period_hypothesis = 3

# the hypothesis refers to the same time period and interest rate as the premise, but it mentions a different investment amount
if investment_amount_premise <= investment_amount_hypothesis:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif interest_rate_premise!= interest_rate_hypothesis or time_period_premise!= time_period_hypothesis:
    # check if the interest rate or time period in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and the premise values are the same, we can infer entailment
    label = "entailment"

print(label)
