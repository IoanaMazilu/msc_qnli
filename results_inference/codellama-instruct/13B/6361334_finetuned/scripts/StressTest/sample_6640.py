work_days_premise = 20
work_days_hypothesis = 40

# the hypothesis refers to the number of days it takes for Ram and Krish to complete the work, which is also mentioned in the premise
if work_days_hypothesis <= work_days_premise:
    # check if the estimate of 'work_days_hypothesis' contradicts the number of days in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days it takes for Ram and Krish to complete the work
    # any number of days greater than 'work_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
