work_hours_premise = 8
work_hours_hypothesis = 6

# the hypothesis refers to the number of hours Dan works before stopping, which is also mentioned in the premise
if work_hours_premise <= work_hours_hypothesis:
    # check if the estimate of 'work_hours_hypothesis' contradicts the number of hours worked by Dan in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the number of hours Dan works before stopping, which is consistent with the hypothesis
    label = "entailment"

print(label)
