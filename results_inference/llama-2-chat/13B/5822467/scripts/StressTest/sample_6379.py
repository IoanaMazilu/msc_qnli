hourly_wage_premise = 10
hourly_wage_hypothesis = 30

# the hypothesis refers to the number of hours for which Harry is paid a certain hourly wage
if hourly_wage_hypothesis <= hourly_wage_premise:
    # check if the hypothesis value contradicts the estimate of 'hourly_wage_premise'
    label = "contradiction"
elif hourly_wage_premise <= hourly_wage_hypothesis * 3:
    # check if the hypothesis value contradicts the estimate of 'hourly_wage_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours for which Harry is paid a certain hourly wage
    # any number of hours greater than 'hourly_wage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
