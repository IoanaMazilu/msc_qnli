payment_premise = 7
payment_hypothesis = 3

# the hypothesis refers to the payment made by Lally that is also mentioned in the premise
if payment_hypothesis >= payment_premise:
    # check if the hypothesis value contradicts the exact payment amount in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
