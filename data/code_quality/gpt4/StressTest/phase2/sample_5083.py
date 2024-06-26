wage_premise = 7.00
wage_hypothesis = 7.00
tip_rate_premise = 6.00
tip_rate_hypothesis = 5.00

# the hypothesis talks about Jill's wage and tip rate, also referenced in the premise
if wage_premise != wage_hypothesis:
    # check if the wage in the hypothesis contradicts the wage reported in the premise
    label = "contradiction"
elif tip_rate_hypothesis >= tip_rate_premise:
    # check if the tip rate in the hypothesis contradicts the estimate of less than 'tip_rate_premise'
    label = "contradiction"
else:
    # if the values in the hypothesis do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
