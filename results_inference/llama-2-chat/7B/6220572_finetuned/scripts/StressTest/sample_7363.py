discount_premise = 10
discount_hypothesis = 30

# the hypothesis refers to the discount on the listed price mentioned in the premise
if discount_hypothesis >= discount_premise:
    # check if the estimate of 'discount_hypothesis' contradicts the discount in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the discount
    # any discount greater than 'discount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
