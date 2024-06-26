below_cost_price_premise = 14
below_cost_price_hypothesis = 24

# the hypothesis talks about the percentage below the cost price at which Vijay sells the cupboard, referenced also in the premise
if below_cost_price_hypothesis != below_cost_price_premise:
    # check if the percentage below cost price in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
