shifts_premise = 36 - 4
shifts_hypothesis = 16
average_orders_premise = 40
average_orders_hypothesis = 40

# the hypothesis talks about the number of shifts and the average orders per hour, referenced also in the premise
if shifts_hypothesis!= shifts_premise:
    # check if the number of shifts in the hypothesis contradicts the number of shifts reported in the premise
    label = "contradiction"
elif average_orders_hypothesis!= average_orders_premise:
    # check if the average orders per hour in the hypothesis contradicts the average orders per hour reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
