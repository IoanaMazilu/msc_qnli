hourly_wage_premise = 8.00
hourly_wage_hypothesis = 8.00
tip_rate_premise = 0.70
tip_rate_hypothesis = 0.30

# the hypothesis refers to the hourly wage and tip rate mentioned in the premise
if hourly_wage_hypothesis!= hourly_wage_premise:
    # check if the hourly wage in the hypothesis contradicts the hourly wage in the premise
    label = "contradiction"
elif tip_rate_hypothesis <= tip_rate_premise:
    # check if the tip rate in the hypothesis contradicts the tip rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
