days_work_premise = 7
days_work_hypothesis = 8

# the hypothesis talks about the number of days it took to complete the work, referenced also in the premise
if days_work_hypothesis <= days_work_premise:
    # check if the hypothesis value contradicts the estimate of more than 'days_work_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days
    # any number of days greater than 'days_work_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
