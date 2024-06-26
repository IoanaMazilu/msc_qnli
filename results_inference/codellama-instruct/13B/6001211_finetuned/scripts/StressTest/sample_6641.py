work_completion_time_premise = 40
work_completion_time_hypothesis = 40

# the hypothesis refers to the time taken by Ram and Krish to complete a work, also mentioned in the premise
if work_completion_time_hypothesis <= work_completion_time_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the premise gives a specific time for the work completion
    # any time longer than 'work_completion_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
