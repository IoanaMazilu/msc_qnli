hours_worked_james_premise = 71
hours_worked_james_hypothesis = 41

# the hypothesis mentions a specific number of hours James worked, which is also referenced in the premise
if hours_worked_james_hypothesis >= hours_worked_james_premise:
    # check if the hypothesis value contradicts the estimate of less than 'hours_worked_james_premise'
    label = "contradiction"
elif hours_worked_james_hypothesis < hours_worked_james_premise:
    # the premise gives only an estimate for the number of hours
    # any number of hours less than 'hours_worked_james_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
