work_time_premise = 70
work_time_hypothesis = 20

# the hypothesis refers to Sakshi's time to finish a piece of work, also mentioned in the premise
if work_time_hypothesis >= work_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'work_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the work time
    # any work time less than 'work_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
