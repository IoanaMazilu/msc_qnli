shifts_hours_premise = 12
shifts_hours_hypothesis = 62
average_orders_hour_premise = 40
average_orders_hour_hypothesis = 40

# the hypothesis refers to the number of hours of shifts and the average orders per hour mentioned in the premise
if shifts_hours_hypothesis < shifts_hours_premise:
    # check if the estimate of'shifts_hours_hypothesis' contradicts the number of hours of shifts in the premise
    label = "contradiction"
elif average_orders_hour_hypothesis!= average_orders_hour_premise:
    # check if the average orders per hour in the hypothesis contradicts the average orders per hour reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
