work_days_together_premise = 12
work_days_together_hypothesis = 52
remaining_work_days_peter = 10

# the hypothesis refers to the number of days they worked together and the number of days Peter worked alone
if work_days_together_premise >= work_days_together_hypothesis:
    # check if the number of days they worked together in the premise contradicts the estimate of less than 'work_days_together_hypothesis'
    label = "contradiction"
elif remaining_work_days_peter!= 10:
    # check if the number of days Peter worked alone in the hypothesis contradicts the number of days Peter worked alone reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
