hourly_rate_premise = 7.00
regular_hours_premise = 40
hourly_rate_hypothesis = 7.00
regular_hours_hypothesis = 30

# the hypothesis refers to the hourly rate and the number of regular hours worked per week mentioned in the premise
if hourly_rate_hypothesis != hourly_rate_premise:
    # check if the hourly rate in the hypothesis contradicts the hourly rate in the premise
    label = "contradiction"
elif regular_hours_hypothesis > regular_hours_premise:
    # check if the number of regular hours in the hypothesis contradicts the number of regular hours in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
