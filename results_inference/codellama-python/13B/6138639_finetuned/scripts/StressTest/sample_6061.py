days_before_work_finished_premise = 1
days_before_work_finished_hypothesis = 7

# the hypothesis talks about the number of days Indu leaves before the work is finished, referenced also in the premise
if days_before_work_finished_hypothesis <= days_before_work_finished_premise:
    # check if the hypothesis value contradicts the estimate of more than 'days_before_work_finished_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days
    # any number of days greater than 'days_before_work_finished_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
