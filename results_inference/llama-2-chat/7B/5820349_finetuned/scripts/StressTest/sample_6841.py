investment_premise = 20000
investment_hypothesis = 20000
months_premise = 7
months_hypothesis = 6

# the hypothesis talks about the same investment and period of time as the premise
if investment_hypothesis!= investment_premise:
    # check if the investment amount in the hypothesis contradicts the investment amount in the premise
    label = "contradiction"
elif months_hypothesis >= months_premise:
    # check if the period of time in the hypothesis contradicts the period of time in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the period of time
    # any period of time less than'months_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
