shifts_worked_premise = 4
shifts_worked_hypothesis = 36 - 4
average_orders_premise = 40
average_orders_hypothesis = 40

# the hypothesis talks about the number of shifts worked, which is also mentioned in the premise
if shifts_worked_hypothesis!= shifts_worked_premise:
    # check if the number of shifts in the hypothesis contradicts the number of shifts in the premise
    label = "contradiction"
elif average_orders_hypothesis!= average_orders_premise:
    # check if the average orders in the hypothesis contradicts the average orders in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
