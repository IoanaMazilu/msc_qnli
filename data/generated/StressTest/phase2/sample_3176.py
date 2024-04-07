# Premise: Molly can do a task in 15 days while Sandy can do the task in 10 days.
# Hypothesis: Molly can do a task in less than 15 days while Sandy can do the task in 10 days.
# Golden Label: contradiction

molly_task_duration_premise = 15
sandy_task_duration_premise = 10
molly_task_duration_hypothesis = 15
sandy_task_duration_hypothesis = 10

# the hypothesis refers to the duration of tasks Molly and Sandy can perform as mentioned in the premise
if molly_task_duration_hypothesis >= molly_task_duration_premise:
    # check if the estimate of 'molly_task_duration_hypothesis' contradicts the duration in the premise
    label = "contradiction"
elif sandy_task_duration_hypothesis != sandy_task_duration_premise:
    # check if the duration for Sandy in the hypothesis contradicts the duration reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

