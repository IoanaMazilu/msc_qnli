hours_paid_x_premise = 40
hours_paid_x_hypothesis = 40

# the hypothesis refers to the number of hours James is paid x dollars per hour, mentioned in the premise
if hours_paid_x_hypothesis <= hours_paid_x_premise:
    # check if the hypothesis value contradicts the number of hours James is paid x dollars per hour in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
