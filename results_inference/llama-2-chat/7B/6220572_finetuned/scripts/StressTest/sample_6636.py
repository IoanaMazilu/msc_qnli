work_days_premise = 30
work_days_hypothesis = 50

# the hypothesis refers to the number of days needed to complete a work, mentioned also in the premise
if work_days_premise >= work_days_hypothesis:
    # check if the estimate of 'work_days_hypothesis' contradicts the number of days in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days
    # any number of days less than 'work_days_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
