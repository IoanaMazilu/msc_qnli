sachi_investment_premise = 5000
sachi_investment_hypothesis = 8000
interest_rate_premise = 5
interest_rate_hypothesis = 5
deposit_time_premise = 2
deposit_time_hypothesis = 2

# the hypothesis talks about the investment amount, interest rate and deposit time, which are also mentioned in the premise
if sachi_investment_hypothesis <= sachi_investment_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif interest_rate_hypothesis!= interest_rate_premise or deposit_time_hypothesis!= deposit_time_premise:
    # check if the interest rate or deposit time in the hypothesis contradicts the premise values
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
