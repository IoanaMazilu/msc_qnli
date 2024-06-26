regular_hours_premise = 30
regular_hours_hypothesis = 30
overtime_rate_premise = 2
overtime_rate_hypothesis = 2

# the hypothesis refers to the pay rate and hours worked per week, mentioned in the premise
if regular_hours_hypothesis >= regular_hours_premise:
    # check if the number of regular hours in the hypothesis contradicts the number of regular hours in the premise
    label = "contradiction"
elif overtime_rate_hypothesis!= overtime_rate_premise:
    # check if the overtime rate in the hypothesis contradicts the overtime rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
