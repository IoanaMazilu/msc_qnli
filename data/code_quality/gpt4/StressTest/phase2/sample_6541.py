leave_time_diff_premise = 10
leave_time_diff_hypothesis = 90

# the hypothesis refers to the time difference between Dan and Cara leaving City A
if leave_time_diff_hypothesis <= leave_time_diff_premise:
    # check if the time difference in the hypothesis contradicts the estimate of more than 'leave_time_diff_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the time difference
    # any time difference greater than 'leave_time_diff_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
