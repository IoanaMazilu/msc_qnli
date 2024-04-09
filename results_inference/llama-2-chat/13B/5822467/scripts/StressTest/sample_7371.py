wage_premise = 10.00
tip_rate_premise = 0.4
hourly_wage_hypothesis = 10.00
tip_rate_hypothesis = 0.8

# the hypothesis refers to the hourly wage and tip rate mentioned in the premise
if hourly_wage_hypothesis <= wage_premise:
    # check if the estimate of 'hourly_wage_hypothesis' contradicts the hourly wage in the premise
    label = "contradiction"
elif tip_rate_hypothesis!= tip_rate_premise:
    # check if the tip rate in the hypothesis contradicts the tip rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
