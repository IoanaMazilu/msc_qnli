hourly_wage_premise = 10.0
tip_rate_premise = 80
tip_rate_hypothesis = 40

# the hypothesis refers to the tip rate as a percentage of the cost of orders served, which is also mentioned in the premise
if tip_rate_hypothesis > tip_rate_premise:
    # check if the tip rate in the hypothesis contradicts the tip rate in the premise
    label = "contradiction"
elif tip_rate_hypothesis < tip_rate_premise:
    # check if the tip rate in the hypothesis is less than the tip rate in the premise
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
