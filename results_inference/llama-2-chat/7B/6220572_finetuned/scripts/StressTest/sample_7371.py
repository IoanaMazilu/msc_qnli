hourly_wage_premise = 10
hourly_wage_hypothesis = 10
tip_rate_premise = 40
tip_rate_hypothesis = 80

# the hypothesis talks about the hourly wage and tip rate of Jill at the local diner, referenced also in the premise
if hourly_wage_hypothesis!= hourly_wage_premise:
    # check if the estimate of 'hourly_wage_hypothesis' contradicts the hourly wage reported in the premise
    label = "contradiction"
elif tip_rate_hypothesis >= tip_rate_premise:
    # check if the tip rate in the hypothesis contradicts the estimate of less than 'tip_rate_premise'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
