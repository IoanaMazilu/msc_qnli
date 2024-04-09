unit_digits_premise = 7
unit_digits_hypothesis = 8

# the hypothesis refers to the product of all possible units digits of Sophie Germain primes greater than 8
if unit_digits_hypothesis <= unit_digits_premise:
    # check if the hypothesis value contradicts the estimate of the product of all possible units digits of Sophie Germain primes greater than 7
    label = "contradiction"
else:
    # the premise gives only an estimate for the product of all possible units digits of Sophie Germain primes greater than 7
    # any product greater than the estimate is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
