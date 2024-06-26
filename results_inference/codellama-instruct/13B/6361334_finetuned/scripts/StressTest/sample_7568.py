shifts_premise = 4
hours_per_shift_premise = 12
orders_per_hour_premise = 40

shifts_hypothesis = 4
hours_per_shift_hypothesis = 42
orders_per_hour_hypothesis = 40

# the hypothesis refers to the number of shifts and hours per shift mentioned in the premise
if shifts_hypothesis!= shifts_premise or hours_per_shift_hypothesis!= hours_per_shift_premise:
    # check if the hypothesis values contradict the premise values
    label = "contradiction"
elif orders_per_hour_hypothesis!= orders_per_hour_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
