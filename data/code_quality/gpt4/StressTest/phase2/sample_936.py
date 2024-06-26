standard_hours_premise = 60
standard_hours_hypothesis = 10
hourly_rate_premise = 6.00
hourly_rate_hypothesis = 6.00

# the hypothesis refers to Sam's pay rate and working hours mentioned in the premise
if standard_hours_hypothesis > standard_hours_premise:
    # check if the number of standard hours in the hypothesis contradicts the number of standard hours in the premise
    label = "contradiction"
elif hourly_rate_hypothesis != hourly_rate_premise:
    # check if the hourly rate in the hypothesis contradicts the hourly rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
