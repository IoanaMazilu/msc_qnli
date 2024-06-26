hourly_wage_premise = 4.00
hourly_wage_hypothesis = 4.00
tip_rate_premise = 15
tip_rate_hypothesis = 15

# the hypothesis refers to the hourly wage and tip rate mentioned in the premise
if hourly_wage_hypothesis != hourly_wage_premise:
    # check if the hourly wage in the hypothesis contradicts the hourly wage reported in the premise
    label = "contradiction"
elif tip_rate_hypothesis > tip_rate_premise:
    # check if the tip rate in the hypothesis contradicts the tip rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment or neutrality
    if tip_rate_hypothesis == tip_rate_premise:
        # if the tip rate in the hypothesis is equal to the tip rate in the premise, we can infer entailment
        label = "entailment"
    else:
        # if the tip rate in the hypothesis is less than the tip rate in the premise, we can infer neutrality
        label = "neutral"

print(label)
