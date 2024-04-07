# Premise: Jane will take only 12 days to complete the same task.
# Hypothesis: Jane will take only less than 62 days to complete the same task.
# Golden Label: entailment

task_completion_premise = 12
task_completion_hypothesis = 62

# the hypothesis talks about the number of days Jane will take to complete a task, referenced also in the premise
if task_completion_hypothesis < task_completion_premise:
    # check if the hypothesis value contradicts the exact number of 'task_completion_premise'
    label = "contradiction"
else:
    # the premise gives an exact number of days for task completion
    # any number of days less than 'task_completion_hypothesis' is consistent with the premise, but the premise does not entail that Jane will take less than 62 days
    label = "entailment"

print(label)

