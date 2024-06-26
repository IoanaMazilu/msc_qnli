work_days_premise = 8
work_days_hypothesis = 6

# the hypothesis refers to the number of days David worked before Moore joined him
if work_days_hypothesis >= work_days_premise:
    # check if the hypothesis value contradicts the estimate of less than 'work_days_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days David worked before Moore joined
    # any number of days less than 'work_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
