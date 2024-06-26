shifts_premise = 4
shifts_hypothesis = 4
hours_per_shift = 8
orders_per_hour = 40

# the hypothesis refers to the number of shifts and hours worked per shift mentioned in the premise
if shifts_hypothesis!= shifts_premise:
    # check if the number of shifts in the hypothesis contradicts the number of shifts reported in the premise
    label = "contradiction"
elif hours_per_shift!= 8 or orders_per_hour!= 40:
    # check if the number of hours worked per shift or the average orders per hour in the hypothesis contradicts the same values reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
