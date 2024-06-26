total_work_days_premise = 20
total_work_days_hypothesis = 30
peter_remaining_work_days_premise = 10
peter_remaining_work_days_hypothesis = 10

# the hypothesis refers to the total number of work days and Peter's work days mentioned in the premise
if total_work_days_premise > total_work_days_hypothesis:
    # check if the estimate of 'total_work_days_premise' contradicts the number of total work days in the hypothesis
    label = "contradiction"
elif peter_remaining_work_days_hypothesis != peter_remaining_work_days_premise:
    # check if the number of Peter's work days in the hypothesis contradicts the number of Peter's work days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
