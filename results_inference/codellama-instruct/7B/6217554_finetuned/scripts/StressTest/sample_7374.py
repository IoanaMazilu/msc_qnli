shifts_worked_premise = 4
shifts_worked_hypothesis = 36
average_orders_hour_premise = 40
average_orders_hour_hypothesis = 40

# the hypothesis refers to the number of shifts worked and the average orders per hour mentioned in the premise
if shifts_worked_hypothesis <= shifts_worked_premise:
    # check if the estimate of'shifts_worked_hypothesis' contradicts the number of shifts worked in the premise
    label = "contradiction"
elif average_orders_hour_hypothesis!= average_orders_hour_premise:
    # check if the average orders per hour in the hypothesis contradicts the average orders per hour reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
