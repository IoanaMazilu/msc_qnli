account_balance_premise = 248
account_balance_hypothesis = 548

# the hypothesis talks about the amount of money in Marie's bank account, referenced also in the premise
if account_balance_hypothesis <= account_balance_premise:
    # check if the hypothesis value contradicts the estimate of less than 'account_balance_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money in Marie's account
    # any amount of money greater than 'account_balance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
