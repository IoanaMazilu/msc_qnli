hourly_wage_premise = 6.00
hourly_wage_hypothesis = 6.00
tip_rate_premise = 75
tip_rate_hypothesis = 35

# the hypothesis refers to the hourly wage and the tip rate mentioned in the premise
if hourly_wage_hypothesis!= hourly_wage_premise:
    # check if the hourly wage in the hypothesis contradicts the hourly wage reported in the premise
    label = "contradiction"
elif tip_rate_hypothesis >= tip_rate_premise:
    # check if the tip rate in the hypothesis contradicts the less than 'tip_rate_premise' estimate
    label = "contradiction"
else:
    # the premise gives only an estimate for the tip rate
    # any tip rate less than 'tip_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
