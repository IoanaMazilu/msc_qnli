working_hours_premise = 6
working_hours_hypothesis = 8

# the hypothesis refers to the number of hours Dan works alone before stopping, which is also the number of hours Annie will take to complete the job
if working_hours_premise <= working_hours_hypothesis:
    # check if the estimate of 'working_hours_hypothesis' contradicts the number of hours worked by Dan in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours Dan works, and any number of hours less than 'working_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
