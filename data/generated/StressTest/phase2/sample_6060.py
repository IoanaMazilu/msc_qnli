# Premise: Anita goes away and Indu leaves 7 days before the work is finished.
# Hypothesis: Anita goes away and Indu leaves more than 1 days before the work is finished.
# Golden Label: entailment

indu_leave_premise = 7
indu_leave_hypothesis = 1

# the hypothesis refers to the number of days Indu leaves before the work is finished mentioned in the premise
if indu_leave_premise < indu_leave_hypothesis:
    # check if the estimate of 'indu_leave_hypothesis' contradicts the number of days Indu leaves before work is finished in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

