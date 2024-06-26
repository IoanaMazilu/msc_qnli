hourly_wage_premise = 4.00
hourly_wage_hypothesis = 4.00
tip_rate_premise = 0.15
tip_rate_hypothesis = 0.45

# the hypothesis talks about the hourly wage and tip rate of Jill, referenced also in the premise
if hourly_wage_hypothesis!= hourly_wage_premise:
    # check if the hourly wage in the hypothesis contradicts the hourly wage reported in the premise
    label = "contradiction"
elif tip_rate_hypothesis!= tip_rate_premise:
    # check if the tip rate in the hypothesis contradicts the tip rate reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the hourly wage
    # any hourly wage greater than 'hourly_wage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
