account_balance_premise = 248
account_balance_hypothesis = 148

# the hypothesis talks about the amount of money in Marie's bank account
if account_balance_hypothesis <= account_balance_premise:
    # check if the hypothesis value contradicts the estimate of the account balance in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money in Marie's account
    # any amount of money greater than 'account_balance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
