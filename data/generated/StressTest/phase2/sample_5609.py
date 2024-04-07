# Premise: Hannah leaves City A 108 minutes after Glen.
# Hypothesis: Hannah leaves City A 608 minutes after Glen.
# Golden Label: contradiction

leave_time_premise = 108
leave_time_hypothesis = 608

# the hypothesis talks about the time difference between Hannah and Glen leaving City A, which is also mentioned in the premise
if leave_time_hypothesis != leave_time_premise:
    # check if the time difference stated in the hypothesis contradicts the time difference stated in the premise
    label = "contradiction"
else:
    # if the hypothesis time difference is equal to the premise time difference, we can infer entailment
    label = "entailment"

print(label)

