hours_worked_premise = 41
hours_worked_hypothesis = 11

# the hypothesis refers to the number of hours worked by James, which is also mentioned in the premise
if hours_worked_premise <= hours_worked_hypothesis:
    # check if the estimate of 'hours_worked_hypothesis' contradicts the number of hours worked in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours worked
    # any number of hours greater than 'hours_worked_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
