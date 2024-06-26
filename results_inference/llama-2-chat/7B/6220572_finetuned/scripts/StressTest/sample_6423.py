account_balance_premise = 248
account_balance_hypothesis = 548

# the hypothesis refers to the number of dollars in Marie's bank account, which is also referenced in the premise
if account_balance_hypothesis >= account_balance_premise:
    # check if the hypothesis value contradicts the number of dollars in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of dollars
    # any number of dollars less than 'account_balance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
