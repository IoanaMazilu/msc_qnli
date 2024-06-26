molly_task_time_premise = 20
sandy_task_time_premise = 30
molly_task_time_hypothesis = 40
sandy_task_time_hypothesis = 30

# the hypothesis refers to the time Molly and Sandy can complete a task, mentioned also in the premise
if molly_task_time_hypothesis < molly_task_time_premise:
    # check if the hypothesis value contradicts the time Molly needs to complete a task in the premise
    label = "contradiction"
elif sandy_task_time_hypothesis != sandy_task_time_premise:
    # check if the time Sandy needs to complete a task in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
