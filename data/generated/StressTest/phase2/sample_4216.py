# Premise: If she worked one more than 1-hour shifts this week and averaged $40 in orders per hour, how much did Jill earn this week?
# Hypothesis: If she worked one 8-hour shifts this week and averaged $40 in orders per hour, how much did Jill earn this week?
# Golden Label: neutral

shift_hours_premise = 1
shift_hours_hypothesis = 8
avg_orders_per_hour = 40

# the hypothesis refers to the number of shift hours worked by Jill, mentioned also in the premise
if shift_hours_hypothesis <= shift_hours_premise:
    # check if the number of shift hours in the hypothesis contradicts the number of shift hours mentioned in the premise
    label = "contradiction"
elif shift_hours_hypothesis > shift_hours_premise:
    # if the number of shift hours in the hypothesis is greater than the one mentioned in the premise
    # this is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

