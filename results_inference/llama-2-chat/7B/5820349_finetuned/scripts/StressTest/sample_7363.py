discount_premise = 10
discount_hypothesis = 30

# the hypothesis refers to the discount on the calculator mentioned in the premise
if discount_hypothesis <= discount_premise:
    # check if the discount percentage in the hypothesis contradicts the estimate of more than 'discount_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the discount
    # any discount percentage greater than 'discount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
