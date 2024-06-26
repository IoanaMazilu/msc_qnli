units_digits_premise = 8
units_digits_hypothesis = 9

# the hypothesis refers to the units digits of Sophie Germain primes, which is also mentioned in the premise
if units_digits_hypothesis <= units_digits_premise:
    # check if the hypothesis value contradicts the estimate of more than 'units_digits_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the units digits
    # any number greater than 'units_digits_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
