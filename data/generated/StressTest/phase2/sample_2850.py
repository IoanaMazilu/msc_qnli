# Premise: Winson earns $10.00 per hour for the first 40 hours he works per week, and twice this rate for overtime.
# Hypothesis: Winson earns $10.00 per hour for the first more than 10 hours he works per week, and twice this rate for overtime.
# Golden Label: entailment

regular_hours_premise = 40
regular_hours_hypothesis = 10
overtime_rate_premise = 2
overtime_rate_hypothesis = 2
hourly_rate = 10

# the hypothesis refers to the regular hours and the overtime rate mentioned in the premise
if regular_hours_hypothesis > regular_hours_premise:
    # check if the 'regular_hours_hypothesis' contradicts the number of regular hours in the premise
    label = "contradiction"
elif overtime_rate_hypothesis != overtime_rate_premise:
    # check if the overtime rate in the hypothesis contradicts the overtime rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

