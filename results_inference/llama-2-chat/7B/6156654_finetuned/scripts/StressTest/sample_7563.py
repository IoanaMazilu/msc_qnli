wage_premise = 8.00
tip_rate_premise = 30
tip_rate_hypothesis = 70

# the hypothesis refers to the tip rate, which is also mentioned in the premise
if tip_rate_hypothesis >= tip_rate_premise:
    # check if the tip rate in the hypothesis contradicts the tip rate in the premise
    label = "contradiction"
elif wage_premise!= 8.00:
    # check if the wage in the premise contradicts the wage in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and the premise values do not contradict, we can infer entailment
    label = "entailment"

print(label)
