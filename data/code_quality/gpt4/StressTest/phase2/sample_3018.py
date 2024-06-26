payment_premise = 128
payment_hypothesis = 628

# the hypothesis refers to the exact payment amount mentioned in the premise
if payment_premise >= payment_hypothesis:
    # check if the 'payment_hypothesis' contradicts the exact payment amount in the premise
    label = "contradiction"
else:
    # if the hypothesis value is greater than the premise value, we cannot infer entailment or contradiction
    label = "neutral"

print(label)
