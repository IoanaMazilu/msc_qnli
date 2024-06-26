shifts_premise = 4
hours_per_shift = 8
orders_per_hour = 40
shifts_hypothesis = 4
hours_per_shift_hypothesis = 8
orders_per_hour_hypothesis = 40

# the hypothesis refers to the number of shifts and the average orders per hour, both mentioned in the premise
if shifts_hypothesis!= shifts_premise:
    # check if the number of shifts in the hypothesis contradicts the number of shifts in the premise
    label = "contradiction"
elif hours_per_shift_hypothesis!= hours_per_shift or orders_per_hour_hypothesis!= orders_per_hour:
    # check if the number of hours per shift or the average orders per hour in the hypothesis contradicts the number of hours per shift or the average orders per hour in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
