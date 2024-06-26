days_task_premise = 16
days_task_hypothesis = 76

# the hypothesis refers to the number of days Mary needs to complete a task, also mentioned in the premise
if days_task_hypothesis <= days_task_premise:
    # check if the hypothesis value contradicts the number of days in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days
    # any number of days greater than 'days_task_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
