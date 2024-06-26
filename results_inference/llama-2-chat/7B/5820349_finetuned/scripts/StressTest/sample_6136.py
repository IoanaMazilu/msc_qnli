hours_worked_james_premise = 61
hours_worked_james_hypothesis = 41

# the hypothesis talks about the number of hours James worked last week, referenced also in the premise
if hours_worked_james_hypothesis >= hours_worked_james_premise:
    # check if the hypothesis value contradicts the estimate of less than 'hours_worked_james_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours James worked
    # any number of hours less than 'hours_worked_james_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
