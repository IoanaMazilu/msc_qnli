# Premise: If she worked five 8-hour shifts this week and averaged $40 in orders per hour, how much did Jill earn this week?
# Hypothesis: If she worked five more than 3-hour shifts this week and averaged $40 in orders per hour, how much did Jill earn this week?
# Golden Label: entailment

shifts_premise = 5
shifts_hypothesis = 3
hours_per_shift = 8
orders_per_hour = 40

# the hypothesis refers to the number of shifts and orders per hour mentioned in the premise
if shifts_premise <= shifts_hypothesis:
    # check if the number of shifts in the hypothesis contradicts the number of shifts mentioned in the premise
    label = "contradiction"
elif hours_per_shift * orders_per_hour * shifts_hypothesis > hours_per_shift * orders_per_hour * shifts_premise:
    # check if the earnings calculated based on the hypothesis data contradicts the earnings calculated from the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

