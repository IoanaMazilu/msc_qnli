# Premise: If she worked four less than 20-hour shifts this week and averaged $40 in orders per hour, how much did Jill earn this week?
# Hypothesis: If she worked four 10-hour shifts this week and averaged $40 in orders per hour, how much did Jill earn this week?
# Golden Label: neutral

shifts_premise = 20 - 4
shifts_hypothesis = 10
orders_per_hour = 40

# the hypothesis talks about the number of hours Jill worked and the orders per hour, referenced also in the premise
if shifts_hypothesis != shifts_premise:
    # check if the number of hours worked in the hypothesis contradicts the number of hours worked in the premise
    label = "contradiction"
elif orders_per_hour != 40:
    # check if the orders per hour in the hypothesis contradicts the orders per hour in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

