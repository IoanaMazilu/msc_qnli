task_completion_time_premise = 16
task_completion_time_hypothesis = 76

# the hypothesis refers to the time Mary needs to complete a task, also mentioned in the premise
if task_completion_time_hypothesis!= task_completion_time_premise:
    # check if the time in the hypothesis contradicts the time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
