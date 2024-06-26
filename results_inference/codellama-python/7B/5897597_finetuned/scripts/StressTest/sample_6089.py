work_together_days_premise = 12
work_together_days_hypothesis = 72
peter_work_days_premise = 10
peter_work_days_hypothesis = 10

# the hypothesis refers to the number of days Matt and Peter worked together and the number of days Peter worked alone, mentioned in the premise
if work_together_days_premise!= work_together_days_hypothesis:
    # check if the number of days Matt and Peter worked together in the hypothesis contradicts the number of days mentioned in the premise
    label = "contradiction"
elif peter_work_days_premise!= peter_work_days_hypothesis:
    # check if the number of days Peter worked alone in the hypothesis contradicts the number of days mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
