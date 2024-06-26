molly_task_time_premise = 15
molly_task_time_hypothesis = 25
sandy_task_time_premise = 10
sandy_task_time_hypothesis = 10

# the hypothesis refers to the time Molly and Sandy can do a task, mentioned also in the premise
if molly_task_time_hypothesis <= molly_task_time_premise:
    # check if the estimate of 'molly_task_time_hypothesis' contradicts the time Molly can do the task in the premise
    label = "contradiction"
elif sandy_task_time_hypothesis != sandy_task_time_premise:
    # check if the time Sandy can do the task in the hypothesis contradicts the time Sandy can do the task reported in the premise
    label = "contradiction"
else:
    # if the hypothesis times do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
