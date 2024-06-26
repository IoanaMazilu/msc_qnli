profit_premise = 22000
profit_hypothesis = 42000

# the hypothesis refers to the profit in the business mentioned in the premise
if profit_premise >= profit_hypothesis:
    # check if the estimate of 'profit_hypothesis' contradicts the profit in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
