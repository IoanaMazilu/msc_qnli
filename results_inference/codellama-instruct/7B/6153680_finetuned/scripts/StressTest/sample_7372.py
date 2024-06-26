wage_hourly_premise = 10.00
wage_hourly_hypothesis = 10.00
tip_rate_premise = 0.80
tip_rate_hypothesis = 0.40

# the hypothesis refers to the same premise, but with a different tip rate
if wage_hourly_premise!= wage_hourly_hypothesis:
    # check if the hourly wage in the hypothesis contradicts the hourly wage in the premise
    label = "contradiction"
elif tip_rate_premise!= tip_rate_hypothesis:
    # check if the tip rate in the hypothesis contradicts the tip rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
