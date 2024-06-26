leave_time_premise = 120
leave_time_hypothesis = 520

# the hypothesis refers to the time Dan leaves City A after Cara, which is also mentioned in the premise
if leave_time_premise > leave_time_hypothesis:
    # check if the premise value contradicts the estimate of less than 'leave_time_hypothesis'
    label = "contradiction"
elif leave_time_premise < leave_time_hypothesis:
    # if the premise value is less than the 'leave_time_hypothesis', we can infer entailment
    label = "entailment"
else:
    # if the premise value is equal to the 'leave_time_hypothesis', it is also consistent with the hypothesis, but cannot be explicitly entailed from the hypothesis
    label = "neutral"

print(label)
