hourly_wage_premise = 10.00
hourly_wage_hypothesis = 10.00
tip_rate_premise = 80
tip_rate_hypothesis = 40

# the hypothesis talks about the hourly wage and tip rate, which are also mentioned in the premise
if hourly_wage_premise!= hourly_wage_hypothesis:
    # check if the hourly wage in the hypothesis contradicts the hourly wage in the premise
    label = "contradiction"
elif tip_rate_premise!= tip_rate_hypothesis:
    # check if the tip rate in the hypothesis contradicts the tip rate in the premise
    label = "contradiction"
else:
    # if the hourly wage and tip rate in the hypothesis do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)