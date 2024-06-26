investment_amount_premise = 8000
investment_amount_hypothesis = 2000
compound_interest_rate_premise = 5
compound_interest_rate_hypothesis = 5
investment_time_premise = 2
investment_time_hypothesis = 2

# the hypothesis talks about the investment amount and interest rate, which are also mentioned in the premise
if investment_amount_hypothesis!= investment_amount_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif compound_interest_rate_hypothesis!= compound_interest_rate_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif investment_time_hypothesis!= investment_time_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
