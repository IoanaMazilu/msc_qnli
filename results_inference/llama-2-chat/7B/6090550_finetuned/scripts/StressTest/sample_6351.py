profit_premise = 22000
profit_hypothesis = 42000

# the hypothesis refers to the profit at the end of the year mentioned in the premise
if profit_hypothesis < profit_premise:
    # check if the profit in the hypothesis contradicts the profit in the premise
    label = "contradiction"
elif profit_premise == 0:
    # check if the profit in the premise is zero
    label = "neutral"
else:
    # if the profit in the premise is not zero, we can infer entailment
    label = "entailment"

print(label)
