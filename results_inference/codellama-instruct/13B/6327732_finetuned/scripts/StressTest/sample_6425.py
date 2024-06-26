account_balance_premise = 248
account_balance_hypothesis = 148

# the hypothesis refers to the account balance mentioned in the premise
if account_balance_hypothesis <= account_balance_premise:
    # check if the estimate of 'account_balance_hypothesis' contradicts the account balance in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the account balance
    # any account balance greater than 'account_balance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
