# Premise: It will take 16 days for Mary to complete a certain task alone.
# Hypothesis: It will take 76 days for Mary to complete a certain task alone.
# Golden Label: contradiction

task_time_premise = 16
task_time_hypothesis = 76

# the hypothesis refers to the time Mary will take to complete a task, as mentioned in the premise
if task_time_hypothesis != task_time_premise:
    # check if the time in the hypothesis contradicts the time mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis time does not contradict the premise time, we can infer entailment
    label = "entailment"

print(label)

