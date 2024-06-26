hours_worked_premise = 41
hours_worked_hypothesis = 40

# the hypothesis talks about the number of hours worked by James last week
if hours_worked_premise <= hours_worked_hypothesis:
    # check if the hypothesis value contradicts the estimate of 'hours_worked_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours worked by James last week
    # any number of hours worked by James last week greater than 'hours_worked_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
