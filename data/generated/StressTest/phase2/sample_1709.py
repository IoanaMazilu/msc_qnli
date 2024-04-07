# Premise: If she worked four 9-hour shifts this week and averaged $40 in orders per hour, how much did Jill earn this week?
# Hypothesis: If she worked four 6-hour shifts this week and averaged $40 in orders per hour, how much did Jill earn this week?
# Golden Label: contradiction

shift_hours_premise = 9
shift_hours_hypothesis = 6
shifts_per_week = 4
earnings_per_hour = 40

# the hypothesis talks about the number of hours Jill worked each shift, which is also referenced in the premise
if shift_hours_hypothesis == shift_hours_premise:
    # check if the hypothesis value contradicts the number of hours worked per shift in the premise
    label = "entailment"
else:
    # the hypothesis suggests a different number of hours worked per shift
    # thus, it cannot be explicitly entailed from the premise, nor does it contradict the premise
    label = "neutral"

print(label)

