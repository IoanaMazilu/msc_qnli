hourly_wage_premise = 5.00
hourly_wage_hypothesis = 5.00
tip_rate_premise = 25
tip_rate_hypothesis = 25

# the hypothesis refers to the hourly wage and tip rate mentioned in the premise
if hourly_wage_premise != hourly_wage_hypothesis:
    # check if the hourly wage in the hypothesis contradicts the wage in the premise
    label = "contradiction"
elif tip_rate_hypothesis >= tip_rate_premise:
    # check if the tip rate in the hypothesis contradicts the tip rate in the premise
    label = "contradiction"
else:
    # if the hourly wage and tip rate in the hypothesis do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
