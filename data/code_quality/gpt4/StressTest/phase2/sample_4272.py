regular_hours_premise = 50
regular_hours_hypothesis = 70
hourly_rate = 7.00

# The hypothesis talks about the number of standard hours and the hourly rate David earns, both also mentioned in the premise
if regular_hours_hypothesis > regular_hours_premise:
    # Check if the number of standard hours in the hypothesis contradicts the number mentioned in the premise
    label = "contradiction"
elif hourly_rate != 7.00:
    # Check if the hourly rate in the hypothesis contradicts the rate mentioned in the premise
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
