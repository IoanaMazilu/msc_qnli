leave_days_premise = 7
leave_days_hypothesis = 7

# the hypothesis refers to the number of days Indu leaves before the work is finished, which is also mentioned in the premise
if leave_days_hypothesis <= leave_days_premise:
    # check if the hypothesis value contradicts the number of days mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
