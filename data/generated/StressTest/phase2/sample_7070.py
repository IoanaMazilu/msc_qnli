# Premise: If she worked two 8-hour shifts this week and averaged $40 in orders per hour, how much did Jill earn this week?
# Hypothesis: If she worked two more than 8-hour shifts this week and averaged $40 in orders per hour, how much did Jill earn this week?
# Golden Label: contradiction

shifts_hours_premise = 8
shifts_hours_hypothesis = 8

# the hypothesis refers to the number of hours per shift mentioned in the premise
if shifts_hours_hypothesis != shifts_hours_premise:
    # check if the number of hours per shift in the hypothesis contradicts the number of hours per shift reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

