regular_hours_premise = 40
regular_hours_hypothesis = 60
overtime_rate_premise = 2
overtime_rate_hypothesis = 2

# the hypothesis refers to the number of regular hours and the pay rate for overtime hours mentioned in the premise
if regular_hours_hypothesis < regular_hours_premise:
    # check if the number of regular hours in the hypothesis contradicts the number of regular hours in the premise
    label = "contradiction"
elif overtime_rate_hypothesis!= overtime_rate_premise:
    # check if the overtime pay rate in the hypothesis contradicts the overtime pay rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
