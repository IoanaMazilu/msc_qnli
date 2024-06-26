indu_leave_premise = 7
indu_leave_hypothesis = 7

# the hypothesis refers to the number of days Indu leaves before the work is finished, mentioned in the premise
if indu_leave_hypothesis <= indu_leave_premise:
    # check if the hypothesis value contradicts the number of days mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
