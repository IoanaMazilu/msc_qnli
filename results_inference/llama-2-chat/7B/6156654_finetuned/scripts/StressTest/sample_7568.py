shift_hours_premise = 48
shift_hours_hypothesis = 42
avg_orders_premise = 40
avg_orders_hypothesis = 40

# the hypothesis refers to the number of shifts and the average orders per hour, which are also mentioned in the premise
if shift_hours_hypothesis!= shift_hours_premise:
    # check if the number of shifts in the hypothesis contradicts the number of shifts in the premise
    label = "contradiction"
elif avg_orders_hypothesis!= avg_orders_premise:
    # check if the average orders per hour in the hypothesis contradicts the average orders per hour in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
