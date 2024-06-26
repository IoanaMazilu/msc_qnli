base_hours_premise = 40
base_hours_hypothesis = 40
overtime_rate_premise = 2
overtime_rate_hypothesis = 2

# the hypothesis refers to the payment rate for the first 40 hours and the overtime rate, both mentioned in the premise
if base_hours_hypothesis >= base_hours_premise:
    # check if the hypothesis value contradicts the premise value for the base hours
    label = "contradiction"
elif overtime_rate_hypothesis!= overtime_rate_premise:
    # check if the overtime rate in the hypothesis contradicts the overtime rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
