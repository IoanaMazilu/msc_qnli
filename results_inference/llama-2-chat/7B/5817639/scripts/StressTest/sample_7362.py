discount_premise = 30
discount_hypothesis = 10

# the hypothesis talks about a discount on a calculator, referenced also in the premise
if discount_hypothesis <= discount_premise:
    # check if the hypothesis value contradicts the estimate of more than 'discount_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the discount,
    # any discount greater than 'discount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
