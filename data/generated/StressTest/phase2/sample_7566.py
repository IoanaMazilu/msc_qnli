# Premise: If she worked four 12-hour shifts this week and averaged $40 in orders per hour, how much did Jill earn this week?
# Hypothesis: If she worked four less than 62-hour shifts this week and averaged $40 in orders per hour, how much did Jill earn this week?
# Golden Label: entailment

shifts_duration_premise = 12 * 4
shifts_duration_hypothesis = 62 * 4
avg_orders_per_hour = 40

# the hypothesis refers to the total hours Jill worked this week, which is also mentioned in the premise
if shifts_duration_hypothesis > shifts_duration_premise:
    # check if the total hours Jill worked this week in the hypothesis contradicts the total hours mentioned in the premise
    label = "contradiction"
elif shifts_duration_hypothesis < shifts_duration_premise:
    # check if the total hours Jill worked this week in the hypothesis is less than the total hours mentioned in the premise
    label = "entailment"
else:
    # if the total hours Jill worked this week in the hypothesis equals the total hours mentioned in the premise
    label = "neutral"

print(label)

