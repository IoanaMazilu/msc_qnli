hours_premise = 24
hours_hypothesis = 54

# the hypothesis talks about the number of hours Harry works each week, referenced also in the premise
if hours_hypothesis <= hours_premise:
    # check if the hypothesis value contradicts the estimate of more than 'hours_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours
    # any number of hours greater than 'hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
