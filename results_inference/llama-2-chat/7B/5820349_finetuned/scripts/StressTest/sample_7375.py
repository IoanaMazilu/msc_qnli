shifts_premise = 36
shifts_hypothesis = 16
average_orders_per_hour = 40

# the hypothesis refers to the number of shifts and the average orders per hour mentioned in the premise
if shifts_hypothesis >= shifts_premise:
    # check if the number of'shifts_hypothesis' contradicts the number of shifts in the premise
    label = "contradiction"
elif average_orders_per_hour!= 40:
    # check if the average orders per hour in the hypothesis contradicts the average orders per hour reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
