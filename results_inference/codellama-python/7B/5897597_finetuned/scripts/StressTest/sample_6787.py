hours_worked_james_premise = 21
hours_worked_james_hypothesis = 41

# the hypothesis refers to the number of hours James worked last week, which is also mentioned in the premise
if hours_worked_james_hypothesis <= hours_worked_james_premise:
    # check if the hypothesis value contradicts the estimate of more than 'hours_worked_james_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours James worked
    # any number of hours greater than 'hours_worked_james_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
