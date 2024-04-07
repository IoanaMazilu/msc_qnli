# Premise: Anita goes away and Indu leaves 7 days before the work is finished.
# Hypothesis: Anita goes away and Indu leaves more than 7 days before the work is finished.
# Golden Label: contradiction

indu_leave_days_premise = 7
indu_leave_days_hypothesis = 7

# the hypothesis discusses the number of days Indu leaves before the work is finished, which is also mentioned in the premise
if indu_leave_days_hypothesis > indu_leave_days_premise:
    # check if the hypothesis value contradicts the exact number of days mentioned in the premise
    label = "contradiction"
elif indu_leave_days_hypothesis < indu_leave_days_premise:
    # check if the hypothesis value contradicts the exact number of days mentioned in the premise
    label = "contradiction"
else:
    # the hypothesis value and the premise value are the same, hence we can infer entailment
    label = "entailment"

print(label)

