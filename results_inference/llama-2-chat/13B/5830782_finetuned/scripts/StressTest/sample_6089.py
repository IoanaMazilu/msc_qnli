total_work_days_premise = 12
total_work_days_hypothesis = 72
peter_remaining_work_days_premise = 10
peter_remaining_work_days_hypothesis = 10

# the hypothesis talks about the total work days, and the remaining work days for Peter, which are also referenced in the premise
if total_work_days_premise!= total_work_days_hypothesis:
    # check if the total work days in the hypothesis contradicts the total work days in the premise
    label = "contradiction"
elif peter_remaining_work_days_premise!= peter_remaining_work_days_hypothesis:
    # check if the remaining work days for Peter in the hypothesis contradicts the remaining work days for Peter in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
