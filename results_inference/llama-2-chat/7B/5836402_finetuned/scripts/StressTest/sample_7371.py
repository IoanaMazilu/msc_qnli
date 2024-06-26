hourly_wage_premise = 10.00
tip_rate_premise = 0.4
tip_rate_hypothesis = 0.8

# the hypothesis refers to the tip rate, which is also mentioned in the premise
if tip_rate_hypothesis >= tip_rate_premise:
    # check if the hypothesis value contradicts the tip rate in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
