task_completion_time_premise = 86
task_completion_time_hypothesis = 16

# the hypothesis talks about the time it takes for Mary to complete a task, referenced also in the premise
if task_completion_time_hypothesis >= task_completion_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'task_completion_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the completion time
    # any completion time less than 'task_completion_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
