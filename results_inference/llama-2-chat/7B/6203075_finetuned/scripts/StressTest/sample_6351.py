profit_premise = 22000
profit_hypothesis = 42000

# the hypothesis refers to the profit mentioned in the premise
if profit_premise >= profit_hypothesis:
    # check if the profit in the premise contradicts the hypothesis
    label = "contradiction"
elif profit_premise < profit_hypothesis:
    # if the profit in the premise is less than the one in the hypothesis, we can infer entailment
    label = "entailment"
else:
    # if the profit in the premise is equal to the one in the hypothesis, we can infer neutrality
    label = "neutral"

print(label)
