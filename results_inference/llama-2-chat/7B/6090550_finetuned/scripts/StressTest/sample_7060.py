leave_time_premise = 20
leave_time_hypothesis = 90

# the hypothesis refers to the time when Dan leaves City A, which is also mentioned in the premise
if leave_time_hypothesis <= leave_time_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is greater than the premise value, we can infer entailment
    label = "entailment"

print(label)
