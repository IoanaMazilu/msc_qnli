# Premise: Molly can do a task in less than 68 days while Sandy can do the task in 12 days.
# Hypothesis: Molly can do a task in 18 days while Sandy can do the task in 12 days.
# Golden Label: neutral

molly_task_days_premise = 68
molly_task_days_hypothesis = 18
sandy_task_days_premise = 12
sandy_task_days_hypothesis = 12

# the hypothesis refers to the time taken by Molly and Sandy to do a task, mentioned in the premise
if molly_task_days_hypothesis >= molly_task_days_premise:
    # check if the hypothesis value contradicts the estimate of less than 'molly_task_days_premise'
    label = "contradiction"
elif sandy_task_days_hypothesis != sandy_task_days_premise:
    # check if the time taken by Sandy in the hypothesis contradicts the time taken by Sandy reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time taken by Molly
    # any number of days less than 'molly_task_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

