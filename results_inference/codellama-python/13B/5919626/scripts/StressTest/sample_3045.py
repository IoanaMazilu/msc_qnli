hours_worked_per_day_premise = 8
hours_worked_per_day_hypothesis = 5

# the hypothesis talks about the number of hours worked per day, referenced also in the premise
if hours_worked_per_day_premise <= hours_worked_per_day_hypothesis:
    # check if the hypothesis value contradicts the estimate of more than 'hours_worked_per_day_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hours worked per day
    # any number of hours worked per day greater than 'hours_worked_per_day_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
