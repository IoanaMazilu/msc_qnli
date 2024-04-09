shifts_premise = 4
shifts_hypothesis = 4
hour_per_shift_premise = 10
hour_per_shift_hypothesis = 70
average_orders_per_hour_premise = 40
average_orders_per_hour_hypothesis = 40

# the hypothesis refers to the number of shifts, hours per shift, and average orders per hour mentioned in the premise
if shifts_hypothesis!= shifts_premise:
    # check if the number of shifts in the hypothesis contradicts the number of shifts reported in the premise
    label = "contradiction"
elif hour_per_shift_hypothesis!= hour_per_shift_premise:
    # check if the hours per shift in the hypothesis contradicts the hours per shift reported in the premise
    label = "contradiction"
elif average_orders_per_hour_hypothesis!= average_orders_per_hour_premise:
    # check if the average orders per hour in the hypothesis contradicts the average orders per hour reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
