discount_premise = 30
discount_hypothesis = 30

# the hypothesis refers to the discount percentage mentioned in the premise
if discount_hypothesis >= discount_premise:
    # check if the estimate of 'discount_hypothesis' contradicts the discount percentage in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the discount percentage
    # any discount percentage less than 'discount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)