# Premise: If she worked four 12-hour shifts this week and averaged $40 in orders per hour, how much did Jill earn this week?
# Hypothesis: If she worked four less than 72-hour shifts this week and averaged $40 in orders per hour, how much did Jill earn this week?
# Golden Label: entailment

shifts_premise = 4
hours_per_shift_premise = 12
hours_per_week_premise = shifts_premise * hours_per_shift_premise

shifts_hypothesis = 4
hours_per_shift_hypothesis = 72 / shifts_hypothesis
hours_per_week_hypothesis = shifts_hypothesis * hours_per_shift_hypothesis

# the hypothesis refers to the same number of shifts and the same rate per hour as the premise
# it also provides a different calculation for the total number of hours worked per week
if hours_per_week_premise != hours_per_week_hypothesis:
    # check if the calculation of 'hours_per_week_hypothesis' contradicts the calculation of 'hours_per_week_premise'
    label = "contradiction"
else:
    # if the calculations in the hypothesis do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

