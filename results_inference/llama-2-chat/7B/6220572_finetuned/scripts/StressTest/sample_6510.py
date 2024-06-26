xy_product_premise = 5
xy_product_hypothesis = 5

# the hypothesis refers to the number of XYZ digits that are divisible by 2, which is also referenced in the premise
if xy_product_hypothesis <= xy_product_premise:
    # check if the hypothesis value contradicts the estimate of more than 'xy_product_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of XYZ digits
    # any number of XYZ digits greater than 'xy_product_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
