unit_digits_premise = 8
unit_digits_hypothesis = 7

# the hypothesis refers to the product of all possible units digits of Sophie Germain primes greater than 7
if unit_digits_hypothesis <= unit_digits_premise:
    # check if the hypothesis value contradicts the estimate of the product of all possible units digits in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the product of all possible units digits
    # any product of all possible units digits greater than unit_digits_premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
