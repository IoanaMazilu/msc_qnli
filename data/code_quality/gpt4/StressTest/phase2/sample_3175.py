molly_task_time_premise = 25
molly_task_time_hypothesis = 15
sandy_task_time_premise = 10
sandy_task_time_hypothesis = 10

# the hypothesis refers to the time Molly and Sandy can do the tasks
if molly_task_time_hypothesis >= molly_task_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'molly_task_time_premise'
    label = "contradiction"
elif sandy_task_time_hypothesis != sandy_task_time_premise:
    # check if the time for Sandy to do the task in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time Molly needs to do the task
    # any number of days less than 'molly_task_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
