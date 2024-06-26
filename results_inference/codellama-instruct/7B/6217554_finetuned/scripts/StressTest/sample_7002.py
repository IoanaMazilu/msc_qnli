work_days_premise = 5
work_days_hypothesis = 3

if work_days_hypothesis >= work_days_premise:
    # check if the estimate of 'work_days_hypothesis' contradicts the number of work days in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of work days
    # any number of work days greater than 'work_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
