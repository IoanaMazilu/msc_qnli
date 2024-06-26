shifts_premise = 2 * 8
shifts_hypothesis = 2 * 8 + 1
average_orders_per_hour = 40

# the hypothesis refers to the number of shifts and average orders per hour mentioned in the premise
if shifts_hypothesis!= shifts_premise:
    # check if the number of shifts in the hypothesis contradicts the number of shifts reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
