account_balance_premise = 248
account_balance_hypothesis = 548

# the hypothesis refers to the account balance of Marie, mentioned in the premise
if account_balance_premise < account_balance_hypothesis:
    # check if the estimate of 'account_balance_hypothesis' contradicts the account balance in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
