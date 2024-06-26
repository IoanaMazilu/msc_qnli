shift_duration_premise = 6 + 4
shift_duration_hypothesis = 8
shifts_premise = 4
shifts_hypothesis = 4
order_per_hour_premise = 40
order_per_hour_hypothesis = 40

# The hypothesis refers to the number of shifts, the duration of each shift and the earnings per hour mentioned in the premise.
if shifts_premise != shifts_hypothesis:
    # Check if the number of shifts in the hypothesis contradicts the number of shifts in the premise
    label = "contradiction"
elif shift_duration_premise != shift_duration_hypothesis:
    # Check if the duration of shifts in the hypothesis contradicts the duration of shifts in the premise
    label = "contradiction"
elif order_per_hour_premise != order_per_hour_hypothesis:
    # Check if the orders per hour in the hypothesis contradicts the orders per hour in the premise
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
