# Premise: Alice leaves City A less than 70 minutes after Bob.
# Hypothesis: Alice leaves City A 30 minutes after Bob.
# Golden Label: neutral

leave_time_difference_premise = 70
leave_time_difference_hypothesis = 30

# the hypothesis refers to the time difference between Alice and Bob leaving City A, also mentioned in the premise
if leave_time_difference_hypothesis >= leave_time_difference_premise:
    # check if the time difference in the hypothesis contradicts the estimate of less than 'leave_time_difference_premise' minutes in the premise
    label = "contradiction"
elif leave_time_difference_hypothesis < leave_time_difference_premise:
    # if the time difference in the hypothesis is less than the time difference in the premise
    # it can be inferred from the premise, thus we infer entailment
    label = "entailment"

print(label)

