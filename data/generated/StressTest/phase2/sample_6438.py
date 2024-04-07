# Premise: If she worked four 10-hour shifts this week and averaged $40 in orders per hour, how much did Jill earn this week?
# Hypothesis: If she worked four less than 20-hour shifts this week and averaged $40 in orders per hour, how much did Jill earn this week?
# Golden Label: entailment

shifts_premise = 10 * 4 # four 10-hour shifts
shifts_hypothesis = 20 * 4 # four 20-hour shifts
average_orders_premise = 40
average_orders_hypothesis = 40

# the hypothesis mentions the length of shifts and average orders made in an hour, which are also specified in the premise
if average_orders_hypothesis != average_orders_premise:
    # check if the average hourly orders in the hypothesis contradicts the average hourly orders in the premise
    label = "contradiction"
elif shifts_hypothesis <= shifts_premise:
    # check if the total hours worked in the hypothesis contradicts the total hours worked in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

