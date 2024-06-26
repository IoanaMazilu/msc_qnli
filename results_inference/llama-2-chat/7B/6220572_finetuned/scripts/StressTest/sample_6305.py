total_hours_premise = 41
total_hours_hypothesis = 61

# the hypothesis refers to the number of hours worked by James last week, also referenced in the premise
if total_hours_hypothesis == total_hours_premise:
    # check if the number of hours worked by James in the hypothesis contradicts the number of hours worked by James reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours worked by James
    # any number of hours greater than 'total_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
