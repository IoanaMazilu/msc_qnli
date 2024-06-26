hours_worked_premise = 41
hours_worked_hypothesis = 71

# the hypothesis refers to the number of hours worked by James and Harry, mentioned in the premise
if hours_worked_premise <= hours_worked_hypothesis:
    # check if the estimate of 'hours_worked_hypothesis' contradicts the number of hours worked by James in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours worked by James
    # any number of hours worked by Harry greater than 'hours_worked_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
