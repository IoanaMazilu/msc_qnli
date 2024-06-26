shifts_premise = 4
hours_per_shift_premise = 10
average_orders_premise = 40

shifts_hypothesis = 4
hours_per_shift_hypothesis = 70
average_orders_hypothesis = 40

# the hypothesis refers to the number of shifts, hours per shift and average orders per hour mentioned in the premise
if shifts_hypothesis!= shifts_premise or hours_per_shift_hypothesis!= hours_per_shift_premise:
    # check if the number of shifts or hours per shift in the hypothesis contradicts the number of shifts or hours per shift in the premise
    label = "contradiction"
elif average_orders_hypothesis!= average_orders_premise:
    # check if the average orders per hour in the hypothesis contradicts the average orders per hour in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
