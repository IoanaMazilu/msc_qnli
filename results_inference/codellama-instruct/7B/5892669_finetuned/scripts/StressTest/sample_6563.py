average_raise_premise = 2
average_raise_hypothesis = 2

# the hypothesis refers to the same situation as the premise, but with a different estimate for the average raise
if average_raise_hypothesis <= average_raise_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
