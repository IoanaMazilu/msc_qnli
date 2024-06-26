hours_worked_premise = 41
hours_worked_hypothesis = 61

# the hypothesis talks about the number of hours worked by James in the last week
# the premise gives the exact number of hours worked by James in the last week
if hours_worked_hypothesis <= hours_worked_premise:
    # check if the hypothesis value contradicts the estimate of 'hours_worked_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours worked by James in the last week
    # any number of hours greater than 'hours_worked_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
