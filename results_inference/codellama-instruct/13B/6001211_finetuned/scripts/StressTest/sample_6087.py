total_work_days_premise = 12 + 10
total_work_days_hypothesis = 52
remaining_work_days_peter_premise = 10
remaining_work_days_peter_hypothesis = 10

# the hypothesis refers to the total number of days and remaining days of work mentioned in the premise
if total_work_days_premise >= total_work_days_hypothesis:
    # check if the estimate of 'total_work_days_hypothesis' contradicts the total number of work days in the premise
    label = "contradiction"
elif remaining_work_days_peter_hypothesis!= remaining_work_days_peter_premise:
    # check if the number of remaining work days in the hypothesis contradicts the number of remaining work days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
