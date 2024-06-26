discount_premise = 30
discount_hypothesis = 0

# the hypothesis talks about a discount on the listed price, which is also referred to in the premise
if discount_hypothesis <= discount_premise:
    # check if the hypothesis value contradicts the estimate of 'discount_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the discount,
    # any discount greater than 'discount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
