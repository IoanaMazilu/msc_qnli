work_days_premise = 7
work_days_hypothesis = 8
task_duration_premise = 14
task_duration_hypothesis = 14

# the hypothesis refers to the number of days Ben worked alone and the duration of the task, both mentioned in the premise
if work_days_hypothesis!= work_days_premise:
    # check if the number of days worked in the hypothesis contradicts the number of days worked reported in the premise
    label = "contradiction"
elif task_duration_hypothesis!= task_duration_premise:
    # check if the duration of the task in the hypothesis contradicts the duration of the task reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
