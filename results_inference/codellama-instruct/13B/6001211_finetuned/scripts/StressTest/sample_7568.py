shifts_premise = 4
shifts_hypothesis = 4
shift_hours_premise = 12
shift_hours_hypothesis = 42
avg_orders_per_hour = 40

# the hypothesis refers to the number of shifts and their duration mentioned in the premise
if shifts_premise!= shifts_hypothesis:
    # check if the number of shifts in the hypothesis contradicts the number of shifts reported in the premise
    label = "contradiction"
elif shift_hours_premise!= shift_hours_hypothesis:
    # check if the duration of the shifts in the hypothesis contradicts the duration of the shifts reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
