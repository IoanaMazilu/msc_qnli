shifts_premise = 5
shifts_hypothesis = 5
hours_per_shift_premise = 8
hours_per_shift_hypothesis = 8
average_order_premise = 40
average_order_hypothesis = 40

# the hypothesis refers to the same work scenario as the premise
if shifts_premise != shifts_hypothesis or hours_per_shift_premise != hours_per_shift_hypothesis or average_order_premise != average_order_hypothesis:
    # check if any of the work conditions described in the hypothesis contradict the ones from the premise
    label = "contradiction"
else:
    # if none of the work conditions contradict, we can infer entailment
    label = "entailment"

print(label)
