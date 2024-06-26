regular_hours_premise = 30
regular_hours_hypothesis = 80
overtime_rate_premise = 2
overtime_rate_hypothesis = 2

# the hypothesis refers to the number of regular hours and the overtime rate mentioned in the premise
if regular_hours_premise!= regular_hours_hypothesis:
    # check if the number of regular hours in the hypothesis contradicts the number of regular hours reported in the premise
    label = "contradiction"
elif overtime_rate_premise!= overtime_rate_hypothesis:
    # check if the overtime rate in the hypothesis contradicts the overtime rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
