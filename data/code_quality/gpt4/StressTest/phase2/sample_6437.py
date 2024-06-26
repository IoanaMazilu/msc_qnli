hourly_wage_premise = 6.00
hourly_wage_hypothesis = 6.00
tip_rate_premise = 35
tip_rate_hypothesis = 65

# the hypothesis refers to the same details about Jill's work as the premise
if hourly_wage_hypothesis != hourly_wage_premise:
    # check if the hourly wage in the hypothesis contradicts the hourly wage in the premise
    label = "contradiction"
elif tip_rate_hypothesis != tip_rate_premise:
    # check if the tip rate in the hypothesis contradicts the tip rate in the premise
    label = "contradiction"
else:
    # if the hourly wage and tip rate in the hypothesis do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
