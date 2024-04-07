# Premise: If she worked six 8-hour shifts this week and averaged $40 in orders per hour, how much did Jill earn this week?
# Hypothesis: If she worked six more than 8-hour shifts this week and averaged $40 in orders per hour, how much did Jill earn this week?
# Golden Label: contradiction

shifts_premise = 6
hours_premise = 8
orders_per_hour_premise = 40

shifts_hypothesis = 6
hours_hypothesis = 8
orders_per_hour_hypothesis = 40

# the hypothesis refers to the number of shifts, hours per shift and orders per hour mentioned in the premise
if shifts_premise != shifts_hypothesis:
    # check if the number of shifts in the hypothesis contradicts the number of shifts in the premise
    label = "contradiction"
elif hours_premise != hours_hypothesis:
    # check if the number of hours per shift in the hypothesis contradicts the number of hours per shift in the premise
    label = "contradiction"
elif orders_per_hour_premise != orders_per_hour_hypothesis:
    # check if the number of orders per hour in the hypothesis contradicts the number of orders per hour in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

