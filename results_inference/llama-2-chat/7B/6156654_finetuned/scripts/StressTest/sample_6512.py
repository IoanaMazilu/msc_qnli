# The hypothesis and premise have different variables and conditions
if xy_product_premise == 3:
    # The hypothesis mentions a different product of X, Y and Z
    label = "contradiction"
elif xy_product_premise!= 7:
    # The hypothesis and premise have different product values
    label = "contradiction"
else:
    # The hypothesis and premise have the same conditions and product values
    label = "entailment"

print(label)
