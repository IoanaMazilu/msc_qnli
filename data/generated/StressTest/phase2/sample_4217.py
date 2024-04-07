# Premise: If she worked one 8-hour shifts this week and averaged $40 in orders per hour, how much did Jill earn this week?
# Hypothesis: If she worked one more than 8-hour shifts this week and averaged $40 in orders per hour, how much did Jill earn this week?
# Golden Label: contradiction

shift_hours_premise = 8
shift_hours_hypothesis = 8 + 1
average_orders_per_hour = 40

# the hypothesis refers to the number of hours Jill worked and the average orders per hour, which are also mentioned in the premise
if shift_hours_hypothesis != shift_hours_premise:
    # check if the number of hours worked by Jill in the hypothesis contradicts the number of hours worked by Jill in the premise
    label = "contradiction"
else:
    # the premise gives the exact number of hours Jill worked and average orders per hour
    # the hypothesis should have the same values to be entailed from the premise
    label = "entailment"

print(label)

