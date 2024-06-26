shifts_premise = 4
shifts_hypothesis = 36
orders_per_hour_premise = 40
orders_per_hour_hypothesis = 40

# the hypothesis refers to the number of shifts and the average orders per hour mentioned in the premise
if shifts_hypothesis < shifts_premise:
    # check if the estimate of'shifts_hypothesis' contradicts the number of shifts in the premise
    label = "contradiction"
elif orders_per_hour_hypothesis!= orders_per_hour_premise:
    # check if the average orders per hour in the hypothesis contradicts the average orders per hour reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
