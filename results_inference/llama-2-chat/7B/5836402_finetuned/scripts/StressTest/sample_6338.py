hourly_wage_premise = 4.0
tip_rate_premise = 0.15
tip_rate_hypothesis = 0.45

# the hypothesis refers to the tip rate, which is also mentioned in the premise
if tip_rate_hypothesis!= tip_rate_premise:
    # check if the tip rate in the hypothesis contradicts the tip rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
