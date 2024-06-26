hourly_wage_premise = 30
hourly_wage_hypothesis = 10

# the hypothesis refers to the number of hours Harry works, referenced also in the premise
if hourly_wage_hypothesis >= hourly_wage_premise:
    # check if the number of hours Harry works in the hypothesis contradicts the number of hours reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours Harry works
    # any number of hours greater than 'hourly_wage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
