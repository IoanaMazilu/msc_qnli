hourly_wage_premise = 6.0
tip_rate_premise = 0.35
tip_rate_hypothesis = 0.65

# the hypothesis refers to the tip rate for the orders served by Jill, which is also mentioned in the premise
if tip_rate_hypothesis!= tip_rate_premise:
    # check if the tip rate in the hypothesis contradicts the tip rate reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
