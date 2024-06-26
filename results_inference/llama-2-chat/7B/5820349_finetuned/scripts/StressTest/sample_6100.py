task_completion_time_premise = 86
task_completion_time_hypothesis = 16

# the hypothesis refers to the time Mary needs to complete a task, which is also mentioned in the premise
if task_completion_time_hypothesis >= task_completion_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'task_completion_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the task completion time
    # any time less than 'task_completion_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
