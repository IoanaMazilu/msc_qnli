total_hours_premise = 61
total_hours_hypothesis = 41

# the hypothesis talks about the number of hours worked by James, referenced also in the premise
if total_hours_premise <= total_hours_hypothesis:
    # check if the estimate of 'total_hours_hypothesis' contradicts the number of hours worked in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours worked
    # any number of hours worked greater than 'total_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
