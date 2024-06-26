hours_worked_premise = 40
hours_worked_hypothesis = 40

# the hypothesis talks about the number of hours worked per week, referenced also in the premise
if hours_worked_hypothesis >= hours_worked_premise:
    # check if the hypothesis value contradicts the estimate of less than 'hours_worked_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours worked
    # any number of hours less than 'hours_worked_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
