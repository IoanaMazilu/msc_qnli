debt_increase_premise = 57
debt_increase_hypothesis = 57
time_period_premise = 7
time_period_hypothesis = 7

# the hypothesis and premise mention the increase in global debt and the time period since the financial crisis
if debt_increase_hypothesis!= debt_increase_premise:
    # check if the increase in global debt in the hypothesis contradicts the increase in global debt in the premise
    label = "contradiction"
elif time_period_hypothesis!= time_period_premise:
    # check if the time period in the hypothesis contradicts the time period in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the increase in global debt
    # any estimate of the increase in global debt in the hypothesis consistent with the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
