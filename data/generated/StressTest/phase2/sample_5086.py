# Premise: If she worked four less than 72-hour shifts this week and averaged $40 in orders per hour, how much did Jill earn this week?
# Hypothesis: If she worked four 12-hour shifts this week and averaged $40 in orders per hour, how much did Jill earn this week?
# Golden Label: neutral

shift_hours_premise = 72
shift_hours_hypothesis = 12
shifts_premise = 4
shifts_hypothesis = 4
order_rate = 40

# the hypothesis refers to the number of shifts and hours per shift mentioned in the premise
if shift_hours_hypothesis != (shift_hours_premise - shifts_premise):
    # check if the hours per shift in the hypothesis contradicts the hours per shift in the premise
    label = "contradiction"
elif shifts_hypothesis != shifts_premise:
    # check if the number of shifts in the hypothesis contradicts the number of shifts in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"


print(label)

