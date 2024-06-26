leave_time_premise = 30
leave_time_hypothesis = 60

# the hypothesis refers to the time Alice leaves City A after Bob, which is also mentioned in the premise
if leave_time_premise > leave_time_hypothesis:
    # check if the premise value contradicts the estimate of less than 'leave_time_hypothesis'
    label = "contradiction"
elif leave_time_premise < leave_time_hypothesis:
    # if the premise value is less than the hypothesis estimate, we can infer entailment
    label = "entailment"
else:
    # if the premise value equals the hypothesis estimate, it is still consistent with the hypothesis, but cannot be explicitly entailed from it
    label = "neutral"

print(label)
