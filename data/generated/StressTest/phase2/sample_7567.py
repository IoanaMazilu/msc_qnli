# Premise: If she worked four less than 62-hour shifts this week and averaged $40 in orders per hour, how much did Jill earn this week?
# Hypothesis: If she worked four 12-hour shifts this week and averaged $40 in orders per hour, how much did Jill earn this week?
# Golden Label: neutral

shifts_length_premise = 62
shifts_length_hypothesis = 12
shifts_number_premise = 4
shifts_number_hypothesis = 4
average_orders_per_hour = 40

# the hypothesis talks about the number and length of shifts worked by Jill this week, referenced also in the premise
if shifts_length_hypothesis != shifts_length_premise - 4:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif shifts_number_hypothesis != shifts_number_premise:
    # check if the number of shifts in the hypothesis contradicts the number of shifts reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

