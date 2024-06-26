account_balance_premise = 248
account_balance_hypothesis = 148

# the hypothesis refers to the amount of money in Marie's bank account, as mentioned in the premise
if account_balance_hypothesis == account_balance_premise:
    # check if the hypothesis value is the same as the premise value
    label = "entailment"
elif account_balance_hypothesis > account_balance_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise but doesn't contradict it, it's neutral
    label = "neutral"

print(label)
