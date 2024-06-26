discount_premise = 30
discount_hypothesis = 10

# the hypothesis refers to the discount on the listed price mentioned in the premise
if discount_hypothesis >= discount_premise:
    # check if the hypothesis value contradicts the discount in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the discount
    # any discount greater than 'discount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
