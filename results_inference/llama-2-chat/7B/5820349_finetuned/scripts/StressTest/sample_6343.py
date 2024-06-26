discount_premise = 588
discount_hypothesis = 288

# the hypothesis refers to the discount amount mentioned in the premise
if discount_hypothesis >= discount_premise:
    # check if the discount amount in the hypothesis contradicts the estimate of less than 'discount_premise'
    label = "contradiction"
elif discount_hypothesis < discount_premise:
    # the premise gives only an estimate for the discount amount
    # any discount amount less than 'discount_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
