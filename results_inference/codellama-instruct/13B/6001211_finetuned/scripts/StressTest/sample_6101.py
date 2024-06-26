task_completion_time_premise = 16
task_completion_time_hypothesis = 76

# the hypothesis refers to the time Mary needs to complete a task alone, also mentioned in the premise
if task_completion_time_hypothesis!= task_completion_time_premise:
    # check if the time estimate in the hypothesis contradicts the time given in the premise
    label = "contradiction"
else:
    # if the time estimates in the hypothesis and premise are the same, we can infer entailment
    label = "entailment"

print(label)
