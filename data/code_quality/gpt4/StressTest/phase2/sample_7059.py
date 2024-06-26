leave_time_diff_premise = 90
leave_time_diff_hypothesis = 20

# the hypothesis talks about the time difference between Dan and Cara's departures from City A, which is also mentioned in the premise
if leave_time_diff_premise < leave_time_diff_hypothesis:
    # check if the 'leave_time_diff_premise' contradicts the estimate of more than 'leave_time_diff_hypothesis'
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
