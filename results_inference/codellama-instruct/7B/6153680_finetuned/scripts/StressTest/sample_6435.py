hourly_wage_premise = 6.00
hourly_wage_hypothesis = 6.00
tip_rate_premise = 0.35
tip_rate_hypothesis = 0.75

# the hypothesis refers to the same premise values
if hourly_wage_premise == hourly_wage_hypothesis and tip_rate_premise == tip_rate_hypothesis:
    # check if the tip rate in the hypothesis contradicts the premise
    if tip_rate_hypothesis >= tip_rate_premise:
        label = "contradiction"
    else:
        label = "entailment"
else:
    label = "neutral"

print(label)
