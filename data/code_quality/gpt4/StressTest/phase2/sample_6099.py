task_completion_time_premise = 16
task_completion_time_hypothesis = 86

# the hypothesis refers to the time Mary needs to complete a task alone, mentioned also in the premise
if task_completion_time_hypothesis <= task_completion_time_premise:
    # check if the hypothesis estimate contradicts the time Mary needs to complete the task alone in the premise
    label = "contradiction"
elif task_completion_time_hypothesis > task_completion_time_premise:
    # if the time required in hypothesis is more than the time specified in premise, it is consistent with the premise
    label = "entailment"

print(label)
