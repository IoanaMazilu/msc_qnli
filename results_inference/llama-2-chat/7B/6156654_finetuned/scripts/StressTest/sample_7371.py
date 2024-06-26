hourly_wage_premise = 10.00
tip_rate_premise = 40
tip_rate_hypothesis = 80

# the hypothesis refers to the tip rate, which is also mentioned in the premise
if tip_rate_hypothesis < tip_rate_premise:
    # check if the tip rate in the hypothesis contradicts the tip rate in the premise
    label = "contradiction"
else:
    # if the tip rate in the hypothesis does not contradict the tip rate in the premise, we can infer entailment
    label = "entailment"

print(label)
