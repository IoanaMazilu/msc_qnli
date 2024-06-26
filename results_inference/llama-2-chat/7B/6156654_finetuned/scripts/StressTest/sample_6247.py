investment_premise = 600000
investment_hypothesis = 100000
interest_rate_premise = 10
interest_rate_hypothesis = 10
time_period_premise = 3
time_period_hypothesis = 3

# the hypothesis talks about the investment and interest rate, which are also mentioned in the premise
if investment_hypothesis <= investment_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif interest_rate_hypothesis!= interest_rate_premise:
    # check if the interest rate in the hypothesis contradicts the interest rate in the premise
    label = "contradiction"
elif time_period_hypothesis!= time_period_premise:
    # check if the time period in the hypothesis contradicts the time period in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
