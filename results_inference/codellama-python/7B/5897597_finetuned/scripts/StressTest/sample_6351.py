profit_premise = 22000
profit_hypothesis = 42000

# the hypothesis refers to the profit mentioned in the premise
if profit_premise >= profit_hypothesis:
    # check if the profit in the premise contradicts the estimate of less than 'profit_hypothesis'
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
