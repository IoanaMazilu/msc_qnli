work_completion_time_premise = 8
work_completion_time_hypothesis = 8

# the hypothesis refers to the time of work completion mentioned in the premise
if work_completion_time_hypothesis <= work_completion_time_premise:
    # check if the estimate of 'work_completion_time_hypothesis' contradicts the time of work completion in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the time of work completion
    # any time greater than 'work_completion_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
