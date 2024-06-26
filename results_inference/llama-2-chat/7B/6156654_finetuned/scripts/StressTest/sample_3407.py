hourly_wage_premise = 4.00
hourly_wage_hypothesis = 4.00
tip_rate_premise = 0.15
tip_rate_hypothesis = 0.65

# the hypothesis refers to the same situation as the premise, but with different values for the hourly wage and tip rate
if hourly_wage_premise!= hourly_wage_hypothesis:
    # check if the hourly wage in the hypothesis contradicts the hourly wage in the premise
    label = "contradiction"
elif tip_rate_premise!= tip_rate_hypothesis:
    # check if the tip rate in the hypothesis contradicts the tip rate in the premise
    label = "contradiction"
else:
    # if the hourly wage and tip rate values in the hypothesis do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
