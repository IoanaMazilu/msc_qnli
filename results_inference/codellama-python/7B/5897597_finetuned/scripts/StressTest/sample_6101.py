task_completion_time_premise = 16
task_completion_time_hypothesis = 76

# the hypothesis refers to the time Mary needs to complete a task alone, mentioned in the premise
if task_completion_time_hypothesis!= task_completion_time_premise:
    # check if the time in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis time does not contradict the premise time, we can infer entailment
    label = "entailment"

print(label)
