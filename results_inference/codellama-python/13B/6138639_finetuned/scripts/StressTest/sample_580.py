leave_time_premise = 60
leave_time_hypothesis = 30

# the hypothesis talks about the time Alice leaves City A, referenced also in the premise
if leave_time_hypothesis >= leave_time_premise:
    # check if the hypothesis value contradicts the estimate of less than 'leave_time_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the leave time
    # any leave time less than 'leave_time_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
