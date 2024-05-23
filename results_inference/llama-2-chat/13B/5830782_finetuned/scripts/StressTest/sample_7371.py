hourly_wage_premise = 10
hourly_wage_hypothesis = 10
tip_rate_premise = 40
tip_rate_hypothesis = 80

# the hypothesis refers to the hourly wage and tip rate of Jill mentioned in the premise
if hourly_wage_premise!= hourly_wage_hypothesis:
    # check if the hourly wage in the hypothesis contradicts the hourly wage reported in the premise
    label = "contradiction"
elif tip_rate_premise >= tip_rate_hypothesis:
    # check if the tip rate in the hypothesis contradicts the tip rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)