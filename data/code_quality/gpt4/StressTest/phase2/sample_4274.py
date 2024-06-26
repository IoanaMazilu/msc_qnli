base_hours_premise = 50
base_hours_hypothesis = 50
base_rate_premise = 7.00
base_rate_hypothesis = 7.00

# the hypothesis refers to the base hours and rate mentioned in the premise
if base_hours_hypothesis >= base_hours_premise:
    # check if the statement of 'base_hours_hypothesis' contradicts the number of base hours in the premise
    label = "contradiction"
elif base_rate_hypothesis != base_rate_premise:
    # check if the hourly rate in the hypothesis contradicts the hourly rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and statements do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
