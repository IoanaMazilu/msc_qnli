hours_worked_premise = 41
hours_worked_hypothesis = 11

# the hypothesis talks about the number of hours worked by James, which is also referenced in the premise
if hours_worked_premise <= hours_worked_hypothesis:
    # check if the estimate of 'hours_worked_hypothesis' contradicts the number of hours worked in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours worked by James
    # any number of hours worked by James consistent with the premise is neutral, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
