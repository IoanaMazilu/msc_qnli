discount_premise = 20
discount_hypothesis = 50

# the hypothesis refers to the discount percentage and the amount each person paid less
if discount_hypothesis <= discount_premise:
    # check if the hypothesis value contradicts the estimate of 'discount_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the discount percentage
    # any discount percentage greater than 'discount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
