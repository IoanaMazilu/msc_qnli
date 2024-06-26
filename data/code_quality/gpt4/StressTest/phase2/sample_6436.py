hourly_wage_premise = 6.00
hourly_wage_hypothesis = 6.00
tip_rate_premise = 0.75
tip_rate_hypothesis = 0.35

# the hypothesis refers to Jill's hourly wage and tip rate mentioned in the premise
if hourly_wage_premise != hourly_wage_hypothesis:
    # check if the hourly wage in the hypothesis contradicts the hourly wage in the premise
    label = "contradiction"
elif tip_rate_hypothesis >= tip_rate_premise:
    # check if the tip rate in the hypothesis contradicts the premise's estimate of less than 'tip_rate_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
