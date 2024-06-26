leave_time_premise = 60
leave_time_hypothesis = 30

# the hypothesis talks about the time difference between Dan and Cara leaving City A
if leave_time_premise < leave_time_hypothesis:
    # check if the premise value contradicts the hypothesis estimate of more than 'leave_time_hypothesis'
    label = "contradiction"
elif leave_time_premise > leave_time_hypothesis:
    # check if the premise value is greater than the hypothesis estimate
    label = "entailment"
else:
    # if the premise value is equal to the hypothesis estimate, it is consistent with the hypothesis but cannot be explicitly entailed from it
    label = "neutral"

print(label)
