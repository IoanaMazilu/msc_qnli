units_digit_product_premise = 3
units_digit_product_hypothesis = 1

# the hypothesis refers to the product of all possible units digits of Sophie Germain primes, mentioned in the premise

if units_digit_product_hypothesis >= units_digit_product_premise:
    # check if the hypothesis value contradicts the premise stating that the product is greater than 'units_digit_product_premise'
    label = "contradiction"
elif units_digit_product_hypothesis < units_digit_product_premise:
    # the premise provides a specific lower bound for the product of units digits
    # any product lower than 'units_digit_product_premise' can be consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
