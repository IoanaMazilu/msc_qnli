sachi_investment_premise = 5000
sachi_investment_hypothesis = 8000
sachi_interest_rate_premise = 5
sachi_interest_rate_hypothesis = 5
sachi_investment_time_premise = 2
sachi_investment_time_hypothesis = 2

# the hypothesis refers to the amount invested and the interest rate mentioned in the premise
if sachi_investment_hypothesis <= sachi_investment_premise:
    # check if the estimate of'sachi_investment_hypothesis' contradicts the amount invested in the premise
    label = "contradiction"
elif sachi_interest_rate_hypothesis!= sachi_interest_rate_premise:
    # check if the interest rate in the hypothesis contradicts the interest rate reported in the premise
    label = "contradiction"
elif sachi_investment_time_hypothesis!= sachi_investment_time_premise:
    # check if the time in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
