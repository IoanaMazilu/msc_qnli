work_days_premise = 7
work_days_hypothesis = 8
task_completion_days_premise = 14
task_completion_days_hypothesis = 14

# the hypothesis refers to the number of days Ben worked and the number of days it will take him to complete the task alone before Blake joined, both mentioned in the premise
if work_days_hypothesis!= work_days_premise:
    # check if the number of work days in the hypothesis contradicts the number of work days reported in the premise
    label = "contradiction"
elif task_completion_days_hypothesis!= task_completion_days_premise:
    # check if the number of days it will take Ben to complete the task alone before Blake joined in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
