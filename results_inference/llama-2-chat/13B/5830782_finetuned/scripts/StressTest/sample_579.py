leave_time_premise = 30
leave_time_hypothesis = 60

# the hypothesis talks about the time Alice leaves City A after Bob, referenced also in the premise
if leave_time_premise > leave_time_hypothesis:
    # check if the premise value contradicts the estimate of less than 'leave_time_hypothesis'
    label = "contradiction"
elif leave_time_premise == leave_time_hypothesis:
    # check if the premise value contradicts the estimate of less than 'leave_time_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
