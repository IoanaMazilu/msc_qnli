shifts_premise = 4
shifts_hypothesis = 6
hour_per_shift = 8
orders_per_hour = 40

# the hypothesis talks about the number of shifts and the average orders per hour, which are also referenced in the premise
if shifts_premise != shifts_hypothesis + 4:
    # check if the number of shifts in the hypothesis contradicts the number of shifts reported in the premise
    label = "contradiction"
elif orders_per_hour != 40:
    # check if the average orders per hour in the hypothesis contradicts the average orders per hour reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
