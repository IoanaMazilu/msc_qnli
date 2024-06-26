worked_shifts_premise = 4
average_orders_premise = 40
worked_shifts_hypothesis = 4 - 62
average_orders_hypothesis = 40

# the hypothesis refers to the number of shifts and the average orders per hour, which are also mentioned in the premise
if worked_shifts_premise!= worked_shifts_hypothesis:
    # check if the number of shifts in the hypothesis contradicts the number of shifts in the premise
    label = "contradiction"
elif average_orders_premise!= average_orders_hypothesis:
    # check if the average orders per hour in the hypothesis contradicts the average orders per hour in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
