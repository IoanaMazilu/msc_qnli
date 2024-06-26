interest_rate_premise = 4
interest_rate_hypothesis = 4
time_premise = 2
time_hypothesis = 1

# the hypothesis talks about the time and interest rate mentioned in the premise
if time_hypothesis <= time_premise:
    # check if the hypothesis value contradicts the estimate of more than 'time_premise'
    label = "contradiction"
elif interest_rate_hypothesis!= interest_rate_premise:
    # check if the interest rate in the hypothesis contradicts the interest rate in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time and interest rate
    # any combination of time and interest rate greater than 'time_premise' and 'interest_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
