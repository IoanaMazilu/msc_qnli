leave_time_diff_premise = 90
leave_time_diff_hypothesis = 20

# the hypothesis refers to the time difference between Dan and Cara leaving City A
if leave_time_diff_premise <= leave_time_diff_hypothesis:
    # check if the time difference in the premise contradicts the estimate of more than 'leave_time_diff_hypothesis'
    label = "contradiction"
else:
    # if the time difference in the premise does not contradict the estimate in the hypothesis, we can infer entailment
    label = "entailment"

print(label)
