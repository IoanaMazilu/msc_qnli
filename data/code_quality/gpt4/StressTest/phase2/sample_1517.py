john_profit_premise = 800
john_profit_hypothesis = 800

# the hypothesis refers to the difference in profit John made more than Mike, mentioned in the premise
if john_profit_hypothesis != john_profit_premise:
    # check if the profits mentioned in the hypothesis contradicts the profit reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
