account_balance_premise = 248
account_balance_hypothesis = 148

# the hypothesis refers to the number of dollars in Marie's bank account mentioned in the premise
if account_balance_hypothesis!= account_balance_premise:
    # check if the number of dollars in the hypothesis contradicts the number of dollars reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
