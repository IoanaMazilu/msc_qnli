hourly_wage_premise = 10.00
hourly_wage_hypothesis = 10.00
tip_rate_premise = 0.80
tip_rate_hypothesis = 0.40

# the hypothesis talks about the hourly wage and tip rate of Jill, referenced also in the premise
if hourly_wage_hypothesis!= hourly_wage_premise:
    # check if the hourly wage in the hypothesis contradicts the hourly wage reported in the premise
    label = "contradiction"
elif tip_rate_hypothesis > tip_rate_premise:
    # check if the tip rate in the hypothesis contradicts the estimate of less than 'tip_rate_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the tip rate
    # any tip rate less than 'tip_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
