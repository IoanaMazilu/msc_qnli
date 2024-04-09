hourly_wage_premise = 100
hourly_wage_hypothesis = 150

# the hypothesis talks about the hourly wage for a certain number of hours, referenced also in the premise
if hourly_wage_hypothesis <= hourly_wage_premise:
    # check if the hypothesis value contradicts the estimate of the hourly wage in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the hourly wage for a certain number of hours, but the hypothesis gives a different number of hours
    # any hourly wage greater than the estimate in the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
