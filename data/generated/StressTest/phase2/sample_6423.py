# Premise: Marie has 248 $in her account of the bank.
# Hypothesis: Marie has less than 548 $in her account of the bank.
# Golden Label: entailment

marie_account_premise = 248
marie_account_hypothesis = 548

# the hypothesis refers to the amount in Marie's bank account mentioned in the premise
if marie_account_premise >= marie_account_hypothesis:
    # check if the estimate of 'marie_account_hypothesis' contradicts the amount in Marie's account in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

