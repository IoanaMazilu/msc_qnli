profit_premise = 22000
profit_hypothesis = 42000

# the hypothesis refers to the profit mentioned in the premise
if profit_premise < profit_hypothesis:
    # check if the profit in the premise contradicts the hypothesis
    label = "contradiction"
else:
    # if the profit in the premise does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
