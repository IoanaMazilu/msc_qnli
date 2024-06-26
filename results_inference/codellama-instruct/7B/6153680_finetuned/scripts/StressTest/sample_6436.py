wage_hourly_premise = 6.00
wage_hourly_hypothesis = 6.00
tip_rate_premise = 0.75
tip_rate_hypothesis = 0.35

# the hypothesis refers to the same wage and tip rate mentioned in the premise
if wage_hourly_hypothesis!= wage_hourly_premise:
    # check if the hourly wage in the hypothesis contradicts the wage in the premise
    label = "contradiction"
elif tip_rate_hypothesis >= tip_rate_premise:
    # check if the tip rate in the hypothesis contradicts the tip rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
