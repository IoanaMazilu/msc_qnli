shifts_premise = 4
shifts_hypothesis = 4
hours_per_shift_premise = 8
hours_per_shift_hypothesis = 8
orders_per_hour = 40

# the hypothesis is talking about the same scenario as the premise
if shifts_premise != shifts_hypothesis:
    # check if the number of shifts in the hypothesis contradicts the number of shifts in the premise
    label = "contradiction"
elif hours_per_shift_hypothesis > hours_per_shift_premise:
    # check if the number of hours per shift in the hypothesis contradicts the number of hours per shift in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
