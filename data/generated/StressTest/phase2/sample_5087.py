# Premise: If she worked four 12-hour shifts this week and averaged $40 in orders per hour, how much did Jill earn this week?
# Hypothesis: If she worked four less than 12-hour shifts this week and averaged $40 in orders per hour, how much did Jill earn this week?
# Golden Label: contradiction

shifts_premise = 4
shift_hours_premise = 12
order_rate_premise = 40

shifts_hypothesis = 4
shift_hours_hypothesis = 12 - 4 # the hypothesis says "four less than 12-hour shifts"
order_rate_hypothesis = 40

# the hypothesis talks about the number of shifts, duration of shifts and order rate that Jill worked on this week
if shifts_premise != shifts_hypothesis:
    # check if the number of shifts in the hypothesis contradicts the number of shifts mentioned in the premise
    label = "contradiction"
elif shift_hours_premise <= shift_hours_hypothesis:
    # check if the duration of shifts in the hypothesis contradicts the duration of shifts mentioned in the premise
    label = "contradiction"
elif order_rate_premise != order_rate_hypothesis:
    # check if the order rate in the hypothesis contradicts the order rate mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

