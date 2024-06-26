profit_premise = 42000
profit_hypothesis = 22000

# the hypothesis refers to the profit mentioned in the premise
if profit_hypothesis >= profit_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, we can infer entailment
    label = "entailment"

print(label)
