account_balance_premise = 248
account_balance_hypothesis = 548

# the hypothesis refers to the account balance of Marie mentioned in the premise
if account_balance_premise >= account_balance_hypothesis:
    # check if the account balance in the premise contradicts the estimate of less than 'account_balance_hypothesis'
    label = "contradiction"
else:
    # if the premise value does not contradict the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
