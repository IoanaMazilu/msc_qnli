molly_task_time_premise = 40
molly_task_time_hypothesis = 20
sandy_task_time_premise = 30
sandy_task_time_hypothesis = 30

# the hypothesis refers to the time Molly and Sandy take to complete a task, as mentioned in the premise
if molly_task_time_hypothesis >= molly_task_time_premise:
    # check if the estimate of 'molly_task_time_hypothesis' contradicts the premise of Molly taking less than 40 days
    label = "contradiction"
elif sandy_task_time_hypothesis != sandy_task_time_premise:
    # check if the time Sandy takes in the hypothesis contradicts the time mentioned in the premise
    label = "contradiction"
else:
    # the premise only gives an estimate for Molly's task time
    # any time less than 'molly_task_time_premise' for Molly is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
