# Premise: Ben worked for 7 days on a task that will take him 14 days to complete alone before he was joined by Blake.
# Hypothesis: Ben worked for 8 days on a task that will take him 14 days to complete alone before he was joined by Blake.
# Golden Label: contradiction

ben_work_days_premise = 7
ben_work_days_hypothesis = 8
task_completion_time = 14

# the hypothesis talks about the task that Ben was working on, referenced also in the premise
if ben_work_days_hypothesis != ben_work_days_premise:
    # check if the number of work days in the hypothesis contradicts the number of work days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

