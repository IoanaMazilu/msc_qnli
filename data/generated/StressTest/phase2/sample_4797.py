# Premise: If she worked six 8-hour shifts this week and averaged $40 in orders per hour, how much did Jill earn this week?
# Hypothesis: If she worked six more than 2-hour shifts this week and averaged $40 in orders per hour, how much did Jill earn this week?
# Golden Label: entailment

shifts_premise = 6
shifts_hypothesis = 2

hour_per_shift = 8
average_order_per_hour = 40

# the hypothesis refers to the work shifts of Jill mentioned in the premise
if shifts_hypothesis != shifts_premise:
    # check if the number of shifts in the hypothesis contradicts the number of shifts in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

