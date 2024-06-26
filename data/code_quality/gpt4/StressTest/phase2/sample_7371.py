hourly_wage_premise = 10.00
hourly_wage_hypothesis = 10.00
tip_rate_premise = 40
tip_rate_hypothesis = 80

# both the hypothesis and premise refer to Jill's hourly wage and tip rate
if hourly_wage_hypothesis != hourly_wage_premise:
    # check if the hourly wage in the hypothesis contradicts the hourly wage mentioned in the premise
    label = "contradiction"
elif tip_rate_hypothesis <= tip_rate_premise:
    # check if the tip rate in the hypothesis contradicts the tip rate mentioned in the premise
    label = "contradiction"
else:
    # the premise gives the exact values for the hourly wage and tip rate
    # any tip rate less than 'tip_rate_hypothesis' and equal to 'hourly_wage_premise' is consistent with the premise but cannot be explicitly entailed from it
    label = "neutral"

print(label)
