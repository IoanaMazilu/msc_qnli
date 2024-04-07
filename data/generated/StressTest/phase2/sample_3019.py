# Premise: If John needs to pay exactly $less than 628, what is the least number of bills he will need to use?
# Hypothesis: If John needs to pay exactly $128, what is the least number of bills he will need to use?
# Golden Label: neutral

payment_premise = 628
payment_hypothesis = 128

# the hypothesis talks about an exact payment amount, referenced also in the premise
if payment_hypothesis >= payment_premise:
    # check if the hypothesis value contradicts the premise of less than 'payment_premise'
    label = "contradiction"
elif payment_hypothesis == payment_premise - 500:
    # check if the hypothesis value can be explicitly entailed from the premise
    label = "entailment"
else:
    # the premise gives an upper limit for the payment
    # any exact payment less than 'payment_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

