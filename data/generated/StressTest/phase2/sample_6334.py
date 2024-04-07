# Premise: Ben worked for more than 2 days on a task that will take him 14 days to complete alone before he was joined by Blake.
# Hypothesis: Ben worked for 7 days on a task that will take him 14 days to complete alone before he was joined by Blake.
# Golden Label: neutral

days_worked_alone_premise = 2
days_worked_alone_hypothesis = 7
task_completion_time = 14

# the hypothesis refers to the number of days Ben worked alone on a task that is also mentioned in the premise
if days_worked_alone_hypothesis <= days_worked_alone_premise:
    # check if the hypothesis value contradicts the estimate of more than 'days_worked_alone_premise'
    label = "contradiction"
elif days_worked_alone_hypothesis > task_completion_time:
    # check if the number of days Ben worked alone in the hypothesis is greater than the total task completion time 
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days Ben worked alone
    # any number of days greater than 'days_worked_alone_premise' and less than or equal to 'task_completion_time' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

