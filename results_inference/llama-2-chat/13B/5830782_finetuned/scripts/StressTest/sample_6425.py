account_balance_premise = 248
account_balance_hypothesis = 148

# the hypothesis refers to the account balance of Marie mentioned in the premise
if account_balance_hypothesis!= account_balance_premise:
    # check if the account balance in the hypothesis contradicts the account balance reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
