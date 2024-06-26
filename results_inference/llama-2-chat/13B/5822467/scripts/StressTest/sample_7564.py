hourly_wage_premise = 8.00
tip_rate_premise = 0.7
hourly_wage_hypothesis = 8.00
tip_rate_hypothesis = 0.3

# the hypothesis refers to the hourly wage and tip rate mentioned in the premise
if hourly_wage_premise == hourly_wage_hypothesis and tip_rate_premise == tip_rate_hypothesis:
    # the hypothesis values and estimates match the premise ones, we can infer entailment
    label = "entailment"
elif hourly_wage_hypothesis > hourly_wage_premise or tip_rate_hypothesis > tip_rate_premise:
    # the hypothesis values contradict the premise estimates, we can infer contradiction
    label = "contradiction"
else:
    # the premise gives only an estimate for the tip rate, any other value is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
