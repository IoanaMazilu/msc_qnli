premise_product = 7
hypothesis_product = 3

# the hypothesis refers to the product of X, Y, and Z, which is also mentioned in the premise
if hypothesis_product!= premise_product:
    # check if the hypothesis value contradicts the product mentioned in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the product of X, Y, and Z
    # any product that is divisible by 2 and has 4 digits is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
