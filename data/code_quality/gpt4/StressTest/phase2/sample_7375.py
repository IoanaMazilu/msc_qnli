shifts_hours_premise = 36
shifts_premise = 4
orders_per_hour = 40

shifts_hours_hypothesis = 16
shifts_hypothesis = 4

# the hypothesis refers to the number of shifts and their duration, as well as the average order value per hour
if shifts_hours_hypothesis != (shifts_hours_premise - 4) or shifts_hypothesis != shifts_premise:
    # check if the numbers of shifts and their duration in the hypothesis contradict the information from the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
