shifts_premise = 8
shifts_hypothesis = 2
orders_per_hour = 40

# the hypothesis refers to the number of shifts and the amount of orders per hour mentioned in the premise
if shifts_premise < shifts_hypothesis:
    # check if the number of 'shifts_hypothesis' contradicts the number of shifts in the premise
    label = "contradiction"
elif shifts_premise == shifts_hypothesis:
    # if the number of shifts in the hypothesis is equal to the number of shifts in the premise, we can infer entailment
    label = "entailment"
else:
    # if the number of shifts in the hypothesis is less than the number of shifts in the premise, but does not contradict the premise, we can infer neutral
    label = "neutral"

print(label)
