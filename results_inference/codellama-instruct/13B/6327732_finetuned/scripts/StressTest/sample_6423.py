account_balance_premise = 248
account_balance_hypothesis = 548

# the hypothesis refers to the account balance mentioned in the premise
if account_balance_premise < account_balance_hypothesis:
    # check if the estimate of 'account_balance_hypothesis' contradicts the account balance in the premise
    label = "contradiction"
else:
    # the premise gives an exact account balance
    # any account balance less than 'account_balance_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
