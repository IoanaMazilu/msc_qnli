work_days_premise = 7
work_days_hypothesis = 2
total_days_task = 14

# the hypothesis refers to the number of days Ben worked on the task, which is also mentioned in the premise
if work_days_hypothesis >= work_days_premise:
    # check if the hypothesis value contradicts the estimate of more than 'work_days_premise' days
    label = "contradiction"
else:
    # if the hypothesis value is less than or equal to 'work_days_premise', it does not contradict the premise, but it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
