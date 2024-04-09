discount_premise = 288
discount_hypothesis = 588

# the hypothesis talks about the true discount on the same sum for the same time
if discount_hypothesis <= discount_premise:
    # check if the hypothesis value contradicts the estimate of Rs. in the premise
    label = "contradiction"
elif discount_hypothesis > discount_premise:
    # the premise gives only an estimate for the true discount
    # any discount greater than Rs. contradicts the premise
    label = "contradiction"
else:
    # the hypothesis value is less than the estimate of Rs. in the premise
    # but the premise does not provide enough information to infer entailment or contradiction
    label = "neutral"

print(label)
