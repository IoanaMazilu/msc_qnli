# Premise: Molly can do a task in less than 70 days while Sandy can do the task in 30 days.
# Hypothesis: Molly can do a task in 10 days while Sandy can do the task in 30 days.
# Golden Label: neutral

molly_task_time_premise = 70
molly_task_time_hypothesis = 10
sandy_task_time_premise = 30
sandy_task_time_hypothesis = 30

# the hypothesis talks about the time Molly and Sandy can complete a task, referenced also in the premise
if molly_task_time_hypothesis >= molly_task_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'molly_task_time_premise'
    label = "contradiction"
elif sandy_task_time_hypothesis != sandy_task_time_premise:
    # check if the time Sandy can complete a task in the hypothesis contradicts the time mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time Molly can complete a task
    # any time less than 'molly_task_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

