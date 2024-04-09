profit_premise = 22000
profit_hypothesis = 42000

# the hypothesis refers to the profit mentioned in the premise
if profit_hypothesis <= profit_premise:
    # check if the estimate of 'profit_hypothesis' contradicts the profit in the premise
    label = "contradiction"
elif profit_premise > profit_hypothesis:
    # check if the profit in the premise contradicts the estimate of 'profit_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
