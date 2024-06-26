shifts_premise = 4
hours_per_shift_premise = 12
orders_per_hour_premise = 40

shifts_hypothesis = 4
hours_per_shift_hypothesis = 42
orders_per_hour_hypothesis = 40

# the hypothesis refers to the same quantities as the premise (number of shifts, hours per shift, orders per hour)
if shifts_hypothesis != shifts_premise:
    # check if the number of shifts in the hypothesis contradicts the number of shifts mentioned in the premise
    label = "contradiction"
elif hours_per_shift_hypothesis != hours_per_shift_premise:
    # check if the number of hours per shift in the hypothesis contradicts the number of hours per shift mentioned in the premise
    label = "contradiction"
elif orders_per_hour_hypothesis != orders_per_hour_premise:
    # check if the number of orders per hour in the hypothesis contradicts the number of orders per hour mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
