hourly_wage_premise = 4.00
hourly_wage_hypothesis = 4.00
tip_rate_premise = 15
tip_rate_hypothesis = 25

# the hypothesis refers to the hourly wage and the tip rate that Jill earns as a waitress, both mentioned also in the premise
if hourly_wage_hypothesis != hourly_wage_premise:
    # check if the hourly wage in the hypothesis contradicts the hourly wage reported in the premise
    label = "contradiction"
elif tip_rate_hypothesis != tip_rate_premise:
    # check if the tip rate in the hypothesis contradicts the tip rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
