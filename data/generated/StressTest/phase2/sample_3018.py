# Premise: If John needs to pay exactly $128, what is the least number of bills he will need to use?
# Hypothesis: If John needs to pay exactly $less than 628, what is the least number of bills he will need to use?
# Golden Label: entailment

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

