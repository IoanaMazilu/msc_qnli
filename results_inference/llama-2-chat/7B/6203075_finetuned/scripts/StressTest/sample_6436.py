hourly_wage_premise = 6.00
hourly_wage_hypothesis = 6.00
tip_rate_premise = 75
tip_rate_hypothesis = 35

# the hypothesis talks about the hourly wage and tip rate of Jill, which are also mentioned in the premise
if hourly_wage_hypothesis!= hourly_wage_premise:
    # check if the hourly wage in the hypothesis contradicts the hourly wage in the premise
    label = "contradiction"
elif tip_rate_hypothesis!= tip_rate_premise:
    # check if the tip rate in the hypothesis contradicts the tip rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
