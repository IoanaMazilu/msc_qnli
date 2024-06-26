work_together_premise = 5
work_together_hypothesis = 5

# the hypothesis talks about the number of days they worked together, referenced also in the premise
if work_together_hypothesis <= work_together_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is greater than the premise value, we can infer entailment
    label = "entailment"

print(label)
