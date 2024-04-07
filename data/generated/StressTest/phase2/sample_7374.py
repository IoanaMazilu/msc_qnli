# Premise: If she worked four 16-hour shifts this week and averaged $40 in orders per hour, how much did Jill earn this week?
# Hypothesis: If she worked four less than 36-hour shifts this week and averaged $40 in orders per hour, how much did Jill earn this week?
# Golden Label: entailment

shifts_duration_premise = 16
shifts_count_premise = 4
hourly_orders_premise = 40

shifts_duration_hypothesis = 36
shifts_count_hypothesis = 4
hourly_orders_hypothesis = 40

# the hypothesis talks about Jill's work duration, shifts count and orders per hour, all also referenced in the premise
if shifts_duration_hypothesis <= shifts_duration_premise:
    # check if the hypothesis value for shifts duration contradicts the premise
    label = "contradiction"
elif shifts_count_hypothesis != shifts_count_premise:
    # check if the hypothesis value for shifts count contradicts the premise
    label = "contradiction"
elif hourly_orders_hypothesis != hourly_orders_premise:
    # check if the hypothesis value for hourly orders contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

