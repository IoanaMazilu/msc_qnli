# Premise: Marie has less than 548 $in her account of the bank.
# Hypothesis: Marie has 248 $in her account of the bank.
# Golden Label: neutral

account_balance_premise = 548
account_balance_hypothesis = 248

# the hypothesis gives a specific value for Marie's account balance, also referenced in the premise
if account_balance_hypothesis >= account_balance_premise:
    # check if the hypothesis value contradicts the premise of having less than 'account_balance_premise'
    label = "contradiction"
else:
    # the premise gives only an upper bound for the account balance
    # any balance less than 'account_balance_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

