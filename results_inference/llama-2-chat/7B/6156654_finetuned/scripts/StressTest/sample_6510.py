# The hypothesis refers to a specific situation described in the premise
if xy_product_premise > 5:
    # If the product of X, Y, and Z is more than 5, which is mentioned in the hypothesis,
    # we can infer entailment
    label = "entailment"
else:
    # If the product of X, Y, and Z is less than or equal to 5, we cannot infer contradiction
    # because the hypothesis does not explicitly contradict the premise
    label = "neutral"

print(label)
