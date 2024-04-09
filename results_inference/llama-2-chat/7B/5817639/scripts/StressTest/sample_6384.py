worked_hours_premise = 45
worked_hours_hypothesis = 55

# the hypothesis talks about the number of hours worked by James, referenced also in the premise
if worked_hours_premise <= worked_hours_hypothesis:
    # check if the estimate of 'worked_hours_hypothesis' contradicts the number of hours worked in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours worked
    # any number of hours worked less than 'worked_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
