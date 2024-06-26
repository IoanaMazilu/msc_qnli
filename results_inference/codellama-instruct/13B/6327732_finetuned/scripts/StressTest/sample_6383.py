hours_per_week_premise = 40
hours_per_week_hypothesis = 50

# the hypothesis talks about the number of hours worked per week, referenced also in the premise
if hours_per_week_hypothesis <= hours_per_week_premise:
    # check if the hypothesis value contradicts the estimate of more than 'hours_per_week_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours worked per week
    # any number of hours greater than 'hours_per_week_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
