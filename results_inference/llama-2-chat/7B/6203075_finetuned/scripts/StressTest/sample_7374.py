shifts_premise = 4
shifts_hypothesis = 36 - 4
average_order_hours_premise = 40
average_order_hours_hypothesis = 40

# the hypothesis refers to the number of shifts worked and the average order hours per shift
if shifts_premise!= shifts_hypothesis:
    # check if the number of shifts in the hypothesis contradicts the number of shifts in the premise
    label = "contradiction"
elif average_order_hours_premise!= average_order_hours_hypothesis:
    # check if the average order hours in the hypothesis contradicts the average order hours in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
