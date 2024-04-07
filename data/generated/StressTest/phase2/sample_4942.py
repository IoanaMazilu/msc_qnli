# Premise: If she worked three more than 4-hour shifts this week and averaged $40 in orders per hour, how much did Jill earn this week?
# Hypothesis: If she worked three 8-hour shifts this week and averaged $40 in orders per hour, how much did Jill earn this week?
# Golden Label: neutral

shifts_worked_premise = 4 + 3
shifts_worked_hypothesis = 8 * 3
orders_per_hour = 40

# the hypothesis refers to the number of shifts Jill worked this week, also mentioned in the premise
if shifts_worked_hypothesis != shifts_worked_premise:
    # check if the number of shifts in the hypothesis contradicts the number of shifts stated in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

