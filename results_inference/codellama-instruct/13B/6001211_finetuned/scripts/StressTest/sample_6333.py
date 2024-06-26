work_days_premise = 7
work_days_hypothesis = 2
task_completion_days_premise = 14
task_completion_days_hypothesis = 14

# the hypothesis refers to the number of days Ben worked and the number of days it will take him to complete the task alone before Blake joined, both mentioned in the premise
if work_days_premise <= work_days_hypothesis:
    # check if the estimate of 'work_days_hypothesis' contradicts the number of work days in the premise
    label = "contradiction"
elif task_completion_days_hypothesis!= task_completion_days_premise:
    # check if the number of task completion days in the hypothesis contradicts the number of task completion days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
