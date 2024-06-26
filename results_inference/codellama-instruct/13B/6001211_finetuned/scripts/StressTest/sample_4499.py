discount_premise = 12
discount_hypothesis = 12

# the hypothesis refers to the discount percentage on the cupboard's cost price mentioned in the premise
if discount_hypothesis <= discount_premise:
    # check if the hypothesis value contradicts the discount percentage in the premise
    label = "contradiction"
else:
    # the premise gives the exact discount percentage
    # any discount percentage greater than 'discount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
