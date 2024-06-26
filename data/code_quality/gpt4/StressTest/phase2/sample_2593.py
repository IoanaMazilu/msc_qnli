work_time_premise = 56
work_time_hypothesis = 26

# the hypothesis refers to the time Mary needs to finish a piece of work, mentioned also in the premise
if work_time_hypothesis >= work_time_premise:
    # check if the hypothesis time contradicts the premise time
    label = "contradiction"
else:
    # the premise provides only an estimate for the time Mary needs to do the work
    # any time less than 'work_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
