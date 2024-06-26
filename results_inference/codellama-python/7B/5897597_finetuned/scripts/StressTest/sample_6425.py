account_balance_premise = 248
account_balance_hypothesis = 148

# the hypothesis refers to the balance of Marie's account mentioned in the premise
if account_balance_hypothesis!= account_balance_premise:
    # check if the balance in the hypothesis contradicts the balance reported in the premise
    label = "contradiction"
else:
    # if the hypothesis balance does not contradict the premise balance, we can infer entailment
    label = "entailment"

print(label)
