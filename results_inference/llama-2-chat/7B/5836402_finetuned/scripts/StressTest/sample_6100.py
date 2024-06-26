days_task_premise = 86
days_task_hypothesis = 16

# the hypothesis refers to the number of days Mary needs to complete a task, mentioned in the premise
if days_task_premise >= days_task_hypothesis:
    # check if the estimate of 'days_task_hypothesis' contradicts the number of days in the premise
    label = "contradiction"
elif days_task_hypothesis < days_task_premise:
    # check if the number of days in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
