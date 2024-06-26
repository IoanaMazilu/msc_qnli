work_days_premise = 7
work_days_hypothesis = 2
task_completion_time_premise = 14
task_completion_time_hypothesis = 14

# the hypothesis refers to the number of days Ben worked and the time the task will take to complete alone
if work_days_premise <= work_days_hypothesis:
    # check if the estimate of 'work_days_hypothesis' contradicts the number of work days in the premise
    label = "contradiction"
elif task_completion_time_premise!= task_completion_time_hypothesis:
    # check if the time the task will take to complete alone in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
