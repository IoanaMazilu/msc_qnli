regular_hours_premise = 10
regular_hours_hypothesis = 60
overtime_rate_premise = 6 * 2
overtime_rate_hypothesis = 6 * 2

# The hypothesis refers to Sam's working hours and pay rate, as stated in the premise
if regular_hours_hypothesis <= regular_hours_premise:
    # Check if the number of regular hours in the hypothesis contradicts the estimate of more than 'regular_hours_premise'
    label = "contradiction"
elif overtime_rate_hypothesis != overtime_rate_premise:
    # Check if the overtime pay rate in the hypothesis contradicts the overtime pay rate reported in the premise
    label = "contradiction"
else:
    # The premise gives only an estimate for the number of regular hours
    # Any number of hours greater than 'regular_hours_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
