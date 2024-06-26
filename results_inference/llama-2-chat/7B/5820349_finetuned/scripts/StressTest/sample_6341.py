shifts_premise = 4
shifts_hypothesis = 4
shift_hours_premise = 8
shift_hours_hypothesis = 8
average_orders_premise = 40
average_orders_hypothesis = 40

# the hypothesis refers to the number of shifts and hours worked, and the average orders per hour, all mentioned in the premise
if shifts_premise!= shifts_hypothesis:
    # check if the number of shifts in the hypothesis contradicts the number of shifts mentioned in the premise
    label = "contradiction"
elif shift_hours_hypothesis!= shift_hours_premise:
    # check if the number of hours in a shift in the hypothesis contradicts the number of hours in a shift mentioned in the premise
    label = "contradiction"
elif average_orders_hypothesis!= average_orders_premise:
    # check if the average orders per hour in the hypothesis contradicts the average orders per hour mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
