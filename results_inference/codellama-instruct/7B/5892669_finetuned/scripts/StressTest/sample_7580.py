work_completion_time_premise = 8
work_completion_time_hypothesis = 8

# the hypothesis refers to the time taken to complete the work, mentioned in the premise
if work_completion_time_hypothesis <= work_completion_time_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
