matt_work_days_premise = 12
matt_work_days_hypothesis = 72
peter_work_days_premise = 10
peter_work_days_hypothesis = 10

# the hypothesis refers to the number of work days of Matt and Peter mentioned in the premise
if matt_work_days_premise!= matt_work_days_hypothesis:
    # check if the number of work days of Matt in the hypothesis contradicts the number of work days reported in the premise
    label = "contradiction"
elif peter_work_days_hypothesis!= peter_work_days_premise:
    # check if the number of work days of Peter in the hypothesis contradicts the number of work days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
