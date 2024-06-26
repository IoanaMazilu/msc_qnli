task_duration_premise = 16
task_duration_hypothesis = 76

# the hypothesis talks about the duration of a task, referenced also in the premise
if task_duration_hypothesis >= task_duration_premise:
    # check if the hypothesis value contradicts the estimate of 'task_duration_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the duration of the task
    # any duration greater than 'task_duration_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
