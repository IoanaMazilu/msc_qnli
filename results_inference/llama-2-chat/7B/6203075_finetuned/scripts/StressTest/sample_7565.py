hourly_wage_premise = 8.00
hourly_wage_hypothesis = 8.00
tip_rate_premise = 30
tip_rate_hypothesis = 30

# the hypothesis talks about the hourly wage and tip rate of Jill at the local diner
if hourly_wage_premise!= hourly_wage_hypothesis:
    # check if the hourly wage in the hypothesis contradicts the hourly wage in the premise
    label = "contradiction"
elif tip_rate_premise!= tip_rate_hypothesis:
    # check if the tip rate in the hypothesis contradicts the tip rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
