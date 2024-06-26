hours_premise = 11
hours_hypothesis = 21

# the hypothesis talks about the number of hours Harry works per week, referenced also in the premise
if hours_hypothesis <= hours_premise:
    # check if the hypothesis value contradicts the estimate of more than 'hours_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours
    # any number of hours greater than 'hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
