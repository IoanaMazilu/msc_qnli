lower_limit_hours_premise = 1
upper_limit_hours_premise = 2
lower_limit_hours_hypothesis = 7
upper_limit_hours_hypothesis = 2

# The hypothesis talks about the number of hours Pat watched television last week, referenced also in the premise
# Check if the values in the hypothesis contradict the ones in the premise
if lower_limit_hours_hypothesis > lower_limit_hours_premise or upper_limit_hours_hypothesis != upper_limit_hours_premise:
    label = "contradiction"
else:
    # The premise gives an estimate for the number of hours
    # The number of hours between 'lower_limit_hours_premise' and 'upper_limit_hours_premise' can be entailed from the premise
    label = "entailment"

print(label)
