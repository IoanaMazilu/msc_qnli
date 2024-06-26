work_days_premise = 50
work_days_hypothesis = 30

# the hypothesis refers to the number of days needed to complete a work, also mentioned in the premise
if work_days_hypothesis >= work_days_premise:
    # check if the estimate of 'work_days_hypothesis' contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days
    # any number of days less than 'work_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)