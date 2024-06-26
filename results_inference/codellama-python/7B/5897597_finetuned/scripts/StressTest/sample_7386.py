work_days_premise = 11
work_days_hypothesis = 81

# the hypothesis refers to the number of days Mary can do a piece of work, mentioned in the premise
if work_days_premise >= work_days_hypothesis:
    # check if the number of days in the premise contradicts the estimate of less than 'work_days_hypothesis'
    label = "contradiction"
else:
    # if the number of days in the premise does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)