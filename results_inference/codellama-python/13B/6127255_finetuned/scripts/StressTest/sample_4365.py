regular_hours_premise = 40
regular_hours_hypothesis = 60
overtime_rate_premise = 2
overtime_rate_hypothesis = 2

# the hypothesis refers to the number of regular hours and the rate of pay for overtime hours mentioned in the premise
if regular_hours_hypothesis < regular_hours_premise:
    # check if the number of regular hours in the hypothesis contradicts the number of regular hours reported in the premise
    label = "contradiction"
elif overtime_rate_hypothesis!= overtime_rate_premise:
    # check if the rate of pay for overtime hours in the hypothesis contradicts the rate of pay for overtime hours reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
