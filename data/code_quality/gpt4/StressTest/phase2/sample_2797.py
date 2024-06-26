task_completion_premise = 62
task_completion_hypothesis = 12

# the hypothesis talks about the time Jane will take to complete a task, referenced also in the premise
if task_completion_hypothesis >= task_completion_premise:
    # check if the hypothesis value contradicts the estimate of less than 'task_completion_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time of task completion
    # any time less than 'task_completion_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
