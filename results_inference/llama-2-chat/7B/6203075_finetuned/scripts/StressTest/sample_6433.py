investment_premise = 5000
investment_hypothesis = 8000
interest_rate_premise = 5
interest_rate_hypothesis = 5
deposit_time_premise = 2
deposit_time_hypothesis = 2

# the hypothesis talks about the amount of investment, interest rate and deposit time, all mentioned in the premise
if investment_hypothesis <= investment_premise:
    # check if the hypothesis value contradicts the estimate of more than 'investment_premise'
    label = "contradiction"
elif interest_rate_hypothesis!= interest_rate_premise or deposit_time_hypothesis!= deposit_time_premise:
    # check if the interest rate or deposit time in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of investment
    # any amount greater than 'investment_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
