account_money_premise = 248
account_money_hypothesis = 548

# the hypothesis refers to the amount of money in Marie's bank account mentioned in the premise
if account_money_premise >= account_money_hypothesis:
    # check if the estimate of 'account_money_hypothesis' contradicts the amount of money in Marie's account in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
