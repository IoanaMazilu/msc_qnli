work_time_premise = 32
work_time_hypothesis = 12

# the hypothesis refers to the time Sakshi takes to complete a work, also mentioned in the premise
if work_time_hypothesis >= work_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'work_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time Sakshi takes
    # any time less than 'work_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
