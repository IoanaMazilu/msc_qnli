work_days_alone_premise = 25
work_days_alone_hypothesis = 75

# the hypothesis refers to the number of work days needed for Sreedhar alone, which is also mentioned in the premise
if work_days_alone_hypothesis <= work_days_alone_premise:
    # check if the hypothesis value contradicts the estimate of more than 'work_days_alone_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of work days
    # any number of work days greater than 'work_days_alone_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
