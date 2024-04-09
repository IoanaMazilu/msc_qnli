hours_worked_james_premise = 41
hours_worked_james_hypothesis = 41

# the hypothesis refers to the number of hours James worked last week, mentioned in the premise
if hours_worked_james_hypothesis >= hours_worked_james_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the premise gives an exact number of hours James worked last week
    # any number of hours less than 'hours_worked_james_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
