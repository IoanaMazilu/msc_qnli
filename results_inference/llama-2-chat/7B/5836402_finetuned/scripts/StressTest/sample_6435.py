hourly_wage_premise = 6.0
tip_rate_premise = 35
tip_rate_hypothesis = 75

# the hypothesis refers to the tip rate, which is also mentioned in the premise
if tip_rate_hypothesis >= tip_rate_premise:
    # check if the tip rate in the hypothesis contradicts the tip rate in the premise
    label = "contradiction"
else:
    # if the tip rate in the hypothesis is less than the one in the premise, we can infer entailment
    label = "entailment"

print(label)
