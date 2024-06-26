account_balance_premise = 248
account_balance_hypothesis = 548

# the hypothesis refers to the balance in Marie's account mentioned in the premise
if account_balance_premise >= account_balance_hypothesis:
    # check if the balance in the premise contradicts the estimate of less than 'account_balance_hypothesis'
    label = "contradiction"
else:
    # if the balance in the premise does not contradict the hypothesis, we can infer entailment
    label = "entailment"

print(label)
