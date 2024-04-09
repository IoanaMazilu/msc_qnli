regular_hours_premise = 24
regular_hours_hypothesis = 54
overtime_rate_premise = 1.5
overtime_rate_hypothesis = 1.5

# the hypothesis refers to the number of regular hours and the overtime rate mentioned in the premise
if regular_hours_hypothesis!= regular_hours_premise:
    # check if the number of regular hours in the hypothesis contradicts the number of regular hours reported in the premise
    label = "contradiction"
elif overtime_rate_hypothesis!= overtime_rate_premise:
    # check if the overtime rate in the hypothesis contradicts the overtime rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
