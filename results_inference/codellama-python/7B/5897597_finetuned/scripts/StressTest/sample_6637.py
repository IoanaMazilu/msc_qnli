work_completion_time_premise = 50
work_completion_time_hypothesis = 30

# the hypothesis talks about the time taken by Ram, Krish and Bhim to complete a work, referenced also in the premise
if work_completion_time_hypothesis >= work_completion_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'work_completion_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time taken to complete a work
    # any time less than 'work_completion_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
