discount_premise = 25
discount_hypothesis = 25

# the hypothesis refers to the discount of the item selected by Christine mentioned in the premise
if discount_hypothesis <= discount_premise:
    # check if the claim of 'discount_hypothesis' contradicts the discount in the premise
    label = "contradiction"
else:
    # the premise gives only an exact discount percentage
    # any discount percentage greater than 'discount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
