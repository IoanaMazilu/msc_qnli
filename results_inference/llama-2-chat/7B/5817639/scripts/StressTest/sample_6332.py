cases_premise = 5
cases_hypothesis = 1

# the hypothesis talks about the number of cases that Kramer can pack in 2 hours, referenced also in the premise
if cases_hypothesis <= cases_premise:
    # check if the hypothesis value contradicts the estimate of 'cases_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of cases
    # any number of cases greater than 'cases_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
