hourly_wage_premise = 8.0
tip_rate_premise = 0.3
tip_rate_hypothesis = 0.3

# the hypothesis refers to the tip rate of Jill mentioned in the premise
if tip_rate_hypothesis >= tip_rate_premise:
    # check if the estimate of 'tip_rate_hypothesis' contradicts the tip rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
