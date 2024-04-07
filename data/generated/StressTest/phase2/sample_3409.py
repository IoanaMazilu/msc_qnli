# Premise: If she worked five more than 3-hour shifts this week and averaged $40 in orders per hour, how much did Jill earn this week?
# Hypothesis: If she worked five 8-hour shifts this week and averaged $40 in orders per hour, how much did Jill earn this week?
# Golden Label: neutral

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

