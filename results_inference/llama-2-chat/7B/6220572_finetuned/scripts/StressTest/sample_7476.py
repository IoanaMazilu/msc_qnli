product_digits_premise = 8
product_digits_hypothesis = 7

# the hypothesis refers to the number of possible units digits of Sophie Germain primes mentioned in the premise
if product_digits_hypothesis >= product_digits_premise:
    # check if the hypothesis value contradicts the number of possible units digits in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of possible units digits
    # any number of possible units digits greater than 'product_digits_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
