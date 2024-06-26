work_days_premise = 8
work_days_hypothesis = 8

# the hypothesis gives an estimate for the number of days the work was completed
if work_days_hypothesis <= work_days_premise:
    # check if the estimate of 'work_days_hypothesis' contradicts the number of days in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days
    # any number of days greater than 'work_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
