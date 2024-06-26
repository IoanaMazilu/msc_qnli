hours_worked_james_premise = 11
hours_worked_james_hypothesis = 41

# the hypothesis refers to the number of hours worked by James mentioned in the premise
if hours_worked_james_hypothesis <= hours_worked_james_premise:
    # check if the estimate of 'hours_worked_james_hypothesis' contradicts the number of hours worked by James in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours worked by James
    # any number of hours greater than 'hours_worked_james_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
