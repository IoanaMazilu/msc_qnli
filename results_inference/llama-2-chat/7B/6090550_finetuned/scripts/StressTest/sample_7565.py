wage_premise = 8.00
wage_hypothesis = 8.00
tip_rate_premise = 0.30
tip_rate_hypothesis = 0.30

# the hypothesis refers to the wage and tip rate of Jill mentioned in the premise
if wage_premise!= wage_hypothesis:
    # check if the wage in the hypothesis contradicts the wage in the premise
    label = "contradiction"
elif tip_rate_hypothesis >= tip_rate_premise:
    # check if the tip rate in the hypothesis contradicts the tip rate in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
