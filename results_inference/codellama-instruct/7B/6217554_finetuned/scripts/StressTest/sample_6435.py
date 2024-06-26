hourly_wage_premise = 6.00
hourly_wage_hypothesis = 75

# the hypothesis talks about the hourly wage of Jill, referenced also in the premise
if hourly_wage_hypothesis >= hourly_wage_premise:
    # check if the tip rate in the hypothesis contradicts the hourly wage in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the hourly wage
    # any hourly wage less than 'hourly_wage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
