# Premise: Hannah leaves City A 108 minutes after Glen.
# Hypothesis: Hannah leaves City A less than 208 minutes after Glen.
# Golden Label: entailment

leave_time_after_glen_premise = 108
leave_time_after_glen_hypothesis = 208

# the hypothesis refers to the time Hannah leaves City A after Glen, which is also mentioned in the premise
if leave_time_after_glen_premise >= leave_time_after_glen_hypothesis:
    # check if the exact time 'leave_time_after_glen_premise' contradicts the estimate of less than 'leave_time_after_glen_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis estimate does not contradict the premise time, we can infer entailment
    label = "entailment"

print(label)

