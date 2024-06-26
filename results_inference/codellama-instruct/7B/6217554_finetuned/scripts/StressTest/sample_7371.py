hourly_wage_premise = 10.00
hourly_wage_hypothesis = 10.00
tip_rate_premise = 0.40
tip_rate_hypothesis = 0.80

# the hypothesis refers to the hourly wage and tip rate mentioned in the premise
if hourly_wage_hypothesis!= hourly_wage_premise:
    # check if the hourly wage in the hypothesis contradicts the hourly wage reported in the premise
    label = "contradiction"
elif tip_rate_hypothesis >= tip_rate_premise:
    # check if the tip rate in the hypothesis contradicts the tip rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)