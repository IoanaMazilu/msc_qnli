worked_days_premise = 7
worked_days_hypothesis = 2
total_days_task_premise = 14
total_days_task_hypothesis = 14

# the hypothesis talks about the number of days Ben worked on a task, which is also mentioned in the premise
if worked_days_hypothesis >= worked_days_premise:
    label = "entailment"
elif worked_days_hypothesis < worked_days_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
