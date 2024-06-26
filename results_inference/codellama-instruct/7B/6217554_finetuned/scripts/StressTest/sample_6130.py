hourly_wage_premise = 11
hourly_wage_hypothesis = 21

# the hypothesis talks about the number of hours Harry works, referenced also in the premise
if hourly_wage_hypothesis <= hourly_wage_premise:
    # check if the hypothesis value contradicts the estimate of more than 'hourly_wage_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours Harry works
    # any number of hours greater than 'hourly_wage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
