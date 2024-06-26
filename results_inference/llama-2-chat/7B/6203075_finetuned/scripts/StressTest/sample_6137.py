hours_worked_premise = 41
hours_worked_hypothesis = 41

# the hypothesis refers to the number of hours James worked last week, which is also mentioned in the premise
if hours_worked_hypothesis >= hours_worked_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, it is consistent with the premise
    # but it cannot be explicitly entailed from the premise, so the label is "neutral"
    label = "neutral"

print(label)
