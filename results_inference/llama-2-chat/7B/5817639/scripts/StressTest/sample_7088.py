working_hours_premise = 6
working_hours_hypothesis = 6

# the hypothesis refers to the number of hours it would take Annie to complete the job if Dan worked alone for less than 6 hours and then stopped
if working_hours_premise <= working_hours_hypothesis:
    # check if the estimate of 'working_hours_hypothesis' contradicts the number of hours worked by Dan in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours, any number of hours less than 'working_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
