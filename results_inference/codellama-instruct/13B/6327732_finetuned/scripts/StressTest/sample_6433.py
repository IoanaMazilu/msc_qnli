investment_premise = 5000
investment_hypothesis = 8000
interest_rate_premise = 5
interest_rate_hypothesis = 5
time_premise = 2
time_hypothesis = 2

# the hypothesis refers to the investment amount and interest rate mentioned in the premise
if investment_hypothesis <= investment_premise:
    # check if the estimate of 'investment_hypothesis' contradicts the investment amount in the premise
    label = "contradiction"
elif interest_rate_hypothesis!= interest_rate_premise:
    # check if the interest rate in the hypothesis contradicts the interest rate reported in the premise
    label = "contradiction"
elif time_hypothesis!= time_premise:
    # check if the time in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
