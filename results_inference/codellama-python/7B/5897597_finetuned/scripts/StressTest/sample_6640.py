work_completion_time_premise = 20
work_completion_time_hypothesis = 40

# the hypothesis refers to the time taken by Ram and Krish to complete a task, which is also mentioned in the premise
if work_completion_time_hypothesis <= work_completion_time_premise:
    # check if the hypothesis value contradicts the estimate of more than 'work_completion_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time taken by Ram and Krish
    # any time greater than 'work_completion_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
