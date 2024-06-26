work_completion_time_ram_krish_premise = 40
work_completion_time_ram_krish_hypothesis = 40

# the hypothesis refers to the time taken by Ram and Krish to complete a task, which is also mentioned in the premise
if work_completion_time_ram_krish_hypothesis <= work_completion_time_ram_krish_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
