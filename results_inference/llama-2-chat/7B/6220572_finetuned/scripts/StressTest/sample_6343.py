discount_premise = 588
discount_hypothesis = 288

# the hypothesis talks about the discount on a sum for the same time, referenced also in the premise
if discount_hypothesis == discount_premise:
    # check if the hypothesis value contradicts the discount on the same sum in the premise
    label = "contradiction"
elif discount_hypothesis < discount_premise:
    # check if the estimate of 'discount_hypothesis' contradicts the discount on the same sum in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the discount
    # any discount greater than 'discount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
