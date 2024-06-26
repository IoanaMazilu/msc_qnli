work_time_premise = 81
work_time_hypothesis = 11

# the hypothesis refers to the time Mary takes to do a piece of work, which is also mentioned in the premise
if work_time_hypothesis >= work_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'work_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time Mary takes to do the work
    # any time less than 'work_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
