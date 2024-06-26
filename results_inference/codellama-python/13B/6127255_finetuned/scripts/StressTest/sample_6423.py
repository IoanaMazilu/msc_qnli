account_balance_premise = 248
account_balance_hypothesis = 548

# the hypothesis refers to the account balance of Marie mentioned in the premise
if account_balance_premise >= account_balance_hypothesis:
    # check if the account balance in the premise contradicts the hypothesis of having less than 'account_balance_hypothesis'
    label = "contradiction"
else:
    # if the account balance in the premise does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
