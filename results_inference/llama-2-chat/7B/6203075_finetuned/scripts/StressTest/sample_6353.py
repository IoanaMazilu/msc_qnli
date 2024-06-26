profit_premise = 22000
profit_hypothesis = 22000

# the hypothesis refers to the profit at the end of the year mentioned in the premise
if profit_hypothesis == profit_premise:
    # if the hypothesis value is equal to the premise value, we can infer entailment
    label = "entailment"
elif profit_hypothesis > profit_premise:
    # if the hypothesis value is greater than the premise value, we can infer contradiction
    label = "contradiction"
else:
    # if the hypothesis value is less than or equal to the premise value, we can infer neutrality
    label = "neutral"

print(label)
