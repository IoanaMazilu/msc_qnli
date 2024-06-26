molly_task_days_premise = 20
sandy_task_days_premise = 30
molly_task_days_hypothesis = 50
sandy_task_days_hypothesis = 30

# the hypothesis refers to the number of days Molly and Sandy take to complete a task, which is also mentioned in the premise
if molly_task_days_premise != molly_task_days_hypothesis:
    # check if the number of days Molly takes to complete a task in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
elif sandy_task_days_premise != sandy_task_days_hypothesis:
    # check if the number of days Sandy takes to complete a task in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)
