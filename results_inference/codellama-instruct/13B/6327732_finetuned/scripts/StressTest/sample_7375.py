shifts_premise = 4
shifts_hypothesis = 4
hours_per_shift_premise = 36
hours_per_shift_hypothesis = 16
orders_per_hour_premise = 40
orders_per_hour_hypothesis = 40

# the hypothesis refers to the number of shifts and hours per shift mentioned in the premise
if shifts_premise!= shifts_hypothesis:
    # check if the number of shifts in the hypothesis contradicts the number of shifts reported in the premise
    label = "contradiction"
elif hours_per_shift_premise!= hours_per_shift_hypothesis:
    # check if the number of hours per shift in the hypothesis contradicts the number of hours per shift reported in the premise
    label = "contradiction"
elif orders_per_hour_premise!= orders_per_hour_hypothesis:
    # check if the average orders per hour in the hypothesis contradicts the average orders per hour reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
